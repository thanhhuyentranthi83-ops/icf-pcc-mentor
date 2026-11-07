import { NextRequest, NextResponse } from "next/server";
import { deleteSession } from "@/lib/serverDb";

export const dynamic = "force-dynamic";

export async function POST(req: NextRequest) {
  try {
    const token = req.cookies.get("hoc_coaching_session")?.value;
    if (token) {
      deleteSession(token);
    }

    const res = NextResponse.json({ success: true });
    res.cookies.delete("hoc_coaching_session");
    return res;
  } catch (err: any) {
    console.error("Logout API error:", err);
    return NextResponse.json({ error: "Lỗi đăng xuất" }, { status: 500 });
  }
}
