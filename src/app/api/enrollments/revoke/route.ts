import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, revokePackage } from "@/lib/serverDb";

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
    const { userId, packageId, reason } = body;

    if (!userId || !packageId) {
      return NextResponse.json({ error: "Thiếu userId hoặc packageId" }, { status: 400 });
    }

    const revoked = revokePackage(userId, packageId, user.email, reason || "");
    if (!revoked) {
      return NextResponse.json({ error: "Không tìm thấy gói học của học viên để thu hồi" }, { status: 404 });
    }

    return NextResponse.json({ success: true, message: "Thu hồi quyền thành công" });
  } catch (err: any) {
    console.error("Enrollment revoke API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}
