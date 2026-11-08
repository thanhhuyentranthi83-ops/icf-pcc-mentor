import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, getPackages, savePackage, deletePackage } from "@/lib/serverDb";
import { PackageRecord } from "@/types";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url);
    const token = req.cookies.get("hoc_coaching_session")?.value;
    const user = token ? getUserBySession(token) : null;
    const isAdmin = user && (user.role === "super_admin" || user.role === "editor" || user.role === "billing");

    // Public gets open packages only unless admin
    const openOnly = searchParams.get("all") === "true" && isAdmin ? false : !isAdmin;
    const packages = getPackages(openOnly);

    return NextResponse.json({ success: true, packages });
  } catch (err: any) {
    console.error("Packages GET API error:", err);
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
    if (!user || user.role !== "super_admin") {
      return NextResponse.json({ error: "Từ chối truy cập: Cần quyền Super Admin" }, { status: 403 });
    }

    const body = (await req.json()) as PackageRecord;
    if (!body.nameVi || !body.allowedCourseIds || !body.allowedFeatures) {
      return NextResponse.json({ error: "Thiếu thông tin gói học viên hợp lệ" }, { status: 400 });
    }

    if (!body.id) {
      body.id = `pkg-${Date.now()}`;
    }

    const saved = savePackage(body);
    return NextResponse.json({ success: true, package: saved });
  } catch (err: any) {
    console.error("Packages POST API error:", err);
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
      return NextResponse.json({ error: "Thiếu ID gói" }, { status: 400 });
    }

    const deleted = deletePackage(id);
    return NextResponse.json({ success: deleted });
  } catch (err: any) {
    console.error("Packages DELETE API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}
