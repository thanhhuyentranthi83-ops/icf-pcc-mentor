import React from "react";
import { NatureIcon as NatureIconType } from "@/types";

interface Props {
  icon: NatureIconType | string;
  className?: string;
  size?: number;
}

export default function NatureIcon({ icon, className = "", size = 20 }: Props) {
  switch (icon) {
    case "seed":
      // Hạt giống (Seed)
      return (
        <svg
          width={size}
          height={size}
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          className={className}
        >
          <path d="M12 2C8 6 6 10 6 14a6 6 0 0 0 12 0c0-4-2-8-6-12Z" />
          <path d="M12 10v6" />
        </svg>
      );
    case "sprout":
      // Chồi non (Sprout)
      return (
        <svg
          width={size}
          height={size}
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          className={className}
        >
          <path d="M7 20h10" />
          <path d="M12 20v-8" />
          <path d="M12 12c-4-4-2-9 4-9 0 6-4 9-4 9Z" />
          <path d="M12 15c-3-2-6-1-7 2 4 1 7-2 7-2Z" />
        </svg>
      );
    case "bamboo":
      // Lá tre / Trúc (Bamboo)
      return (
        <svg
          width={size}
          height={size}
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          className={className}
        >
          <path d="M12 2v20" />
          <path d="M12 8c4-2 7-1 9 1-4 2-7 1-9-1Z" />
          <path d="M12 14c-4-2-7-1-9 1 4 2 7 1 9-1Z" />
          <path d="M10 6h4" />
          <path d="M10 12h4" />
          <path d="M10 18h4" />
        </svg>
      );
    case "lotus":
      // Đóa sen (Lotus)
      return (
        <svg
          width={size}
          height={size}
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          className={className}
        >
          <path d="M12 3c-2 4-3 8 0 13 3-5 2-9 0-13Z" />
          <path d="M7 8c-3 4-2 9 5 10-3-4-3-8-5-10Z" />
          <path d="M17 8c3 4 2 9-5 10 3-4 3-8 5-10Z" />
          <path d="M3 14c0 4 5 6 9 6s9-2 9-6" />
        </svg>
      );
    case "mountain":
    default:
      // Ngọn núi (Mountain)
      return (
        <svg
          width={size}
          height={size}
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          className={className}
        >
          <path d="m8 3 4 8 5-5 5 15H2L8 3z" />
          <path d="M4.14 15.08c2.62-1.57 5.24-1.43 7.86.42 2.74 1.94 5.49 2 8.23.19" />
        </svg>
      );
  }
}
