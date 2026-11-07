import { NextRequest, NextResponse } from "next/server";
import { getUserBySession } from "@/lib/serverDb";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  try {
    const token = req.cookies.get("hoc_coaching_session")?.value;
    if (!token) {
      return NextResponse.json({ authenticated: false, user: null });
    }

    const user = getUserBySession(token);
    if (!user) {
      return NextResponse.json({ authenticated: false, user: null });
    }

    return NextResponse.json({ authenticated: true, user });
  } catch (err: any) {
    console.error("Auth me API error:", err);
    return NextResponse.json({ authenticated: false, user: null }, { status: 500 });
  }
}
