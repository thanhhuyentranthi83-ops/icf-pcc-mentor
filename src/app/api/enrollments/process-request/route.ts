import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, processEnrollmentRequest } from "@/lib/serverDb";

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
    const { requestId, approve, durationDays, note } = body;

    if (!requestId || typeof approve !== "boolean") {
      return NextResponse.json({ error: "Thiếu requestId hoặc approve" }, { status: 400 });
    }

    const processed = processEnrollmentRequest(
      requestId,
      approve,
      user.email,
      typeof durationDays === "number" ? durationDays : 30,
      note || ""
    );

    if (!processed) {
      return NextResponse.json({ error: "Không tìm thấy yêu cầu" }, { status: 404 });
    }

    return NextResponse.json({
      success: true,
      message: approve ? "Đã phê duyệt và cấp gói thành công" : "Đã từ chối yêu cầu",
      request: processed
    });
  } catch (err: any) {
    console.error("Enrollment process-request API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}
