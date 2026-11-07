import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, getAllStudentsForAdmin, getDatabase, saveDatabase } from "@/lib/serverDb";

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

    // Role check: Only super_admin, editor, or billing can access
    if (user.role !== "super_admin" && user.role !== "editor" && user.role !== "billing") {
      return NextResponse.json({ error: "Từ chối truy cập: Bạn không có quyền quản trị" }, { status: 403 });
    }

    const students = getAllStudentsForAdmin();
    return NextResponse.json({ success: true, students });
  } catch (err: any) {
    console.error("Admin students API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const token = req.cookies.get("hoc_coaching_session")?.value;
    if (!token) {
      return NextResponse.json({ error: "Yêu cầu đăng nhập" }, { status: 401 });
    }

    const user = getUserBySession(token);
    if (!user || (user.role !== "super_admin" && user.role !== "billing")) {
      return NextResponse.json({ error: "Từ chối truy cập" }, { status: 403 });
    }

    const body = await req.json();
    const { studentId, tier, tierExpiresAt } = body;

    const db = getDatabase();
    const target = db.users.find(u => u.id === studentId);
    if (!target) {
      return NextResponse.json({ error: "Không tìm thấy học viên" }, { status: 404 });
    }

    if (tier) target.tier = tier;
    if (tierExpiresAt !== undefined) target.tierExpiresAt = tierExpiresAt;

    saveDatabase(db);
    return NextResponse.json({ success: true, user: target });
  } catch (err: any) {
    console.error("Admin students update API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}
