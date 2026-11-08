import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, grantPackage } from "@/lib/serverDb";

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
    const { userId, packageId, durationDays, note } = body;

    if (!userId || !packageId) {
      return NextResponse.json({ error: "Thiếu userId hoặc packageId" }, { status: 400 });
    }

    const enrollment = grantPackage(
      userId,
      packageId,
      typeof durationDays === "number" ? durationDays : 30,
      user.email,
      note || ""
    );

    return NextResponse.json({ success: true, enrollment });
  } catch (err: any) {
    console.error("Enrollment grant API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}
