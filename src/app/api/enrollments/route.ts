import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, getUserEnrollments, getEnrollmentRequests, getEnrollmentHistory, getDatabase } from "@/lib/serverDb";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  try {
    const token = req.cookies.get("hoc_coaching_session")?.value;
    if (!token) {
      return NextResponse.json({ error: "Yêu cầu đăng nhập" }, { status: 401 });
    }

    const user = getUserBySession(token);
    if (!user) {
      return NextResponse.json({ error: "Phiên đăng nhập không hợp lệ" }, { status: 401 });
    }

    const isAdmin = user.role === "super_admin" || user.role === "billing" || user.role === "editor";

    if (!isAdmin) {
      // Student view: only return current user's enrollments, requests, and history
      const enrollments = getUserEnrollments(user.id);
      const requests = getEnrollmentRequests().filter(r => r.userId === user.id);
      const history = getEnrollmentHistory(user.id);

      return NextResponse.json({
        success: true,
        isAdmin: false,
        enrollments,
        requests,
        history
      });
    }

    // Admin view
    const db = getDatabase();
    const requests = getEnrollmentRequests();
    const history = getEnrollmentHistory();

    return NextResponse.json({
      success: true,
      isAdmin: true,
      enrollments: db.enrollments || {},
      requests,
      history
    });
  } catch (err: any) {
    console.error("Enrollments GET API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}
