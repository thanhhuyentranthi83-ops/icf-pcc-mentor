import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, renewPackage } from "@/lib/serverDb";

export const dynamic = "force-dynamic";

export async function POST(req: NextRequest) {
  try {
    const token = req.cookies.get("hoc_coaching_session")?.value;
    if (!token) {
      return NextResponse.json({ error: "Yêu cầu đăng nhập" }, { status: 401 });
    }

    const user = getUserBySession(token);
    if (!user || (user.role !== "super_admin" && user.role !== "billing")) {
      return NextResponse.json({ error: "Từ chối truy cập: Cần quyền Quản trị viên" }, { status: 403 });
    }

    const body = await req.json();
    const { userId, packageId, extensionDays, note } = body;

    if (!userId || !packageId) {
      return NextResponse.json({ error: "Thiếu userId hoặc packageId" }, { status: 400 });
    }

    const enrollment = renewPackage(
      userId,
      packageId,
      typeof extensionDays === "number" ? extensionDays : 30,
      user.email,
      note || ""
    );

    if (!enrollment) {
      return NextResponse.json({ error: "Không tìm thấy gói học của học viên để gia hạn" }, { status: 404 });
    }

    return NextResponse.json({ success: true, enrollment });
  } catch (err: any) {
    console.error("Enrollment renew API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}
