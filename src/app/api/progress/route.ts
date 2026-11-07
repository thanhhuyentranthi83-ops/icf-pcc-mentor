import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, getUserProgress, saveUserLessonProgress } from "@/lib/serverDb";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  try {
    const token = req.cookies.get("hoc_coaching_session")?.value;
    if (!token) {
      return NextResponse.json({ error: "Chưa đăng nhập" }, { status: 401 });
    }

    const user = getUserBySession(token);
    if (!user) {
      return NextResponse.json({ error: "Phiên đăng nhập hết hạn" }, { status: 401 });
    }

    const progressData = getUserProgress(user.id);
    return NextResponse.json({ success: true, ...progressData });
  } catch (err: any) {
    console.error("Progress GET API error:", err);
    return NextResponse.json({ error: "Lỗi tải tiến độ" }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const token = req.cookies.get("hoc_coaching_session")?.value;
    if (!token) {
      return NextResponse.json({ error: "Chưa đăng nhập" }, { status: 401 });
    }

    const user = getUserBySession(token);
    if (!user) {
      return NextResponse.json({ error: "Phiên đăng nhập hết hạn" }, { status: 401 });
    }

    const body = await req.json();
    const { lessonId, status, score, note, needsReview } = body;

    if (!lessonId) {
      return NextResponse.json({ error: "Thiếu lessonId" }, { status: 400 });
    }

    const updated = saveUserLessonProgress(user.id, lessonId, {
      status,
      score,
      note,
      needsReview
    });

    return NextResponse.json({ success: true, ...updated });
  } catch (err: any) {
    console.error("Progress POST API error:", err);
    return NextResponse.json({ error: "Lỗi lưu tiến độ" }, { status: 500 });
  }
}
