import { NextRequest, NextResponse } from "next/server";
import { getUserBySession, mergeGuestProgress } from "@/lib/serverDb";

export const dynamic = "force-dynamic";

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
    const { guestProgress } = body;

    if (!guestProgress || typeof guestProgress !== "object") {
      return NextResponse.json({ error: "Dữ liệu học thử không hợp lệ" }, { status: 400 });
    }

    const result = mergeGuestProgress(user.id, guestProgress);
    return NextResponse.json({ success: true, ...result });
  } catch (err: any) {
    console.error("Progress merge API error:", err);
    return NextResponse.json({ error: "Lỗi gộp tiến độ" }, { status: 500 });
  }
}
