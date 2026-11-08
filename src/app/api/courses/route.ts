import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, getCourses, saveCourse, deleteCourse } from "@/lib/serverDb";
import { CourseRecord } from "@/types";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url);
    const token = req.cookies.get("hoc_coaching_session")?.value;
    const user = token ? getUserBySession(token) : null;
    const isAdmin = user && (user.role === "super_admin" || user.role === "editor" || user.role === "billing");

    // If admin explicitly wants all, or if not specified for admin, show all. If public, show published only.
    const publishedOnly = searchParams.get("all") === "true" && isAdmin ? false : !isAdmin;
    const courses = getCourses(publishedOnly);

    return NextResponse.json({ success: true, courses });
  } catch (err: any) {
    console.error("Courses GET API error:", err);
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
    if (!user || (user.role !== "super_admin" && user.role !== "editor")) {
      return NextResponse.json({ error: "Từ chối truy cập: Cần quyền quản trị khóa học" }, { status: 403 });
    }

    const body = (await req.json()) as CourseRecord;
    if (!body.titleVi || !body.moduleIds || !Array.isArray(body.moduleIds)) {
      return NextResponse.json({ error: "Thiếu thông tin khóa học hợp lệ (titleVi, moduleIds)" }, { status: 400 });
    }

    if (!body.id) {
      body.id = `crs-${Date.now()}`;
    }

    const saved = saveCourse(body);
    return NextResponse.json({ success: true, course: saved });
  } catch (err: any) {
    console.error("Courses POST API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest) {
  try {
    const token = req.cookies.get("hoc_coaching_session")?.value;
    if (!token) {
      return NextResponse.json({ error: "Yêu cầu đăng nhập" }, { status: 401 });
    }

    const user = getUserBySession(token);
    if (!user || user.role !== "super_admin") {
      return NextResponse.json({ error: "Từ chối truy cập: Cần quyền Super Admin" }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const id = searchParams.get("id");
    if (!id) {
      return NextResponse.json({ error: "Thiếu ID khóa học" }, { status: 400 });
    }

    const deleted = deleteCourse(id);
    return NextResponse.json({ success: deleted });
  } catch (err: any) {
    console.error("Courses DELETE API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}
