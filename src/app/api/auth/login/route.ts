import { NextRequest, NextResponse } from "next/server";
import { createOrUpdateUser, createSession } from "@/lib/serverDb";

export const dynamic = "force-dynamic";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { email, fullName } = body;

    if (!email || typeof email !== "string" || !email.includes("@")) {
      return NextResponse.json({ error: "Email không hợp lệ" }, { status: 400 });
    }

    const user = createOrUpdateUser(email, fullName);
    const token = createSession(user.id);

    const res = NextResponse.json({
      success: true,
      user
    });

    // Set secure cookie
    res.cookies.set("hoc_coaching_session", token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === "production",
      sameSite: "lax",
      path: "/",
      maxAge: 30 * 24 * 60 * 60 // 30 days
    });

    return res;
  } catch (err: any) {
    console.error("Login API error:", err);
    return NextResponse.json({ error: "Lỗi xử lý đăng nhập" }, { status: 500 });
  }
}
