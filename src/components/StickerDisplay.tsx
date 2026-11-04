"use client";

import React from "react";
import { Sticker } from "@/types";

interface Props {
  sticker: Sticker;
  className?: string;
  size?: number;
  message?: string;
}

export default function StickerDisplay({ sticker, className = "", size = 96, message }: Props) {
  return (
    <div className={`flex flex-col items-center text-center p-3 ${className}`}>
      <div
        style={{ width: size, height: size }}
        className="transition-transform hover:scale-105"
        dangerouslySetInnerHTML={{ __html: sticker.svgContent }}
      />
      {message && (
        <p className="mt-2 text-xs font-serif italic text-zen-ink/90 max-w-xs leading-relaxed">
          {message}
        </p>
      )}
    </div>
  );
}
