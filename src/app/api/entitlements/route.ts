import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, checkUserEntitlement, getUserEnrollments } from "@/lib/serverDb";
import { FeatureKey } from "@/types";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url);
    const courseId = searchParams.get("courseId") || undefined;
    const moduleId = searchParams.get("moduleId") || undefined;
    const lessonId = searchParams.get("lessonId") || undefined;
    const feature = (searchParams.get("feature") as FeatureKey) || undefined;

    const token = req.cookies.get("hoc_coaching_session")?.value;
    const user = token ? getUserBySession(token) : null;

    const result = checkUserEntitlement(user ? user.id : null, {
      courseId,
      moduleId,
      lessonId,
      feature
    });

    const userEnrollments = user ? getUserEnrollments(user.id) : [];

    return NextResponse.json({
      success: true,
      authenticated: !!user,
      userRole: user?.role || "guest",
      ...result,
      enrollments: userEnrollments
    });
  } catch (err: any) {
    console.error("Entitlements check API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { courseId, moduleId, lessonId, feature } = body;

    const token = req.cookies.get("hoc_coaching_session")?.value;
    const user = token ? getUserBySession(token) : null;

    const result = checkUserEntitlement(user ? user.id : null, {
      courseId,
      moduleId,
      lessonId,
      feature
    });

    const userEnrollments = user ? getUserEnrollments(user.id) : [];

    return NextResponse.json({
      success: true,
      authenticated: !!user,
      userRole: user?.role || "guest",
      ...result,
      enrollments: userEnrollments
    });
  } catch (err: any) {
    console.error("Entitlements POST API error:", err);
    return NextResponse.json({ error: "Lỗi máy chủ" }, { status: 500 });
  }
}
