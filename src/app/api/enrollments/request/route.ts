import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, createEnrollmentRequest } from "@/lib/serverDb";

export const dynamic = "force-dynamic";

export async function POST(req: NextRequest) {
  try {
    const token = req.cookies.get("hoc_coaching_session")?.value;
    if (!token) {
      return NextResponse.json({ error: "Yêu cầu đăng nhập để gửi yêu cầu" }, { status: 401 });
    }

    const user = getUserBySession(token);
    if (!user) {
      return NextResponse.json({ error: "Phiên đăng nhập không hợp lệ" }, { status: 401 });
    }

    const body = await req.json();
    const { packageId, type, userNote } = body;

    if (!packageId) {
      return NextResponse.json({ error: "Thiếu packageId" }, { status: 400 });
    }

    const request = createEnrollmentRequest(
      user.id,
      packageId,
      type === "renew" ? "renew" : "register",
      userNote || ""
    );

    return NextResponse.json({
      success: true,
      message: type === "renew" ? "Đã gửi yêu cầu gia hạn đến ban quản trị" : "Đã gửi yêu cầu đăng ký khóa học",
      request
    });
  } catch (err: any) {
    console.error("Enrollment request API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}
