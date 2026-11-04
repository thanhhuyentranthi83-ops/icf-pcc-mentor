import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        zen: {
          bg: "#F7F3EA",         // Giấy dó kem
          paper: "#FAF7F2",      // Trắng giấy ấm
          surface: "#F0EAE1",    // Nền thẻ nhẹ
          border: "#E2D9CC",     // Viền mềm
          moss: "#8BA888",       // Xanh rêu lá trà nhạt
          "moss-dark": "#4F6F52", // Xanh rêu trầm
          "moss-deep": "#3A533D", // Xanh rêu đậm
          lotus: "#E8A0B4",      // Hồng sen điểm xuyết
          "lotus-light": "#F6D6DF", // Hồng cánh sen non
          ochre: "#D9A441",      // Vàng nghệ CTA
          "ochre-dark": "#B88427",
          wood: "#6B4F3A",       // Nâu gỗ mộc
          ink: "#2F3A32",        // Mực than đen dịu
          muted: "#667769",      // Xám rêu nhẹ
          night: {
            bg: "#1E2621",       // Đêm thiền - nền chính
            surface: "#26322B",  // Đêm thiền - card surface
            border: "#33433A",   // Đêm thiền - viền
            text: "#EDE8DC",     // Đêm thiền - chữ ngà
            muted: "#96A699"     // Đêm thiền - chữ phụ
          }
        }
      },
      fontFamily: {
        serif: ["var(--font-lora)", "Lora", "Noto Serif", "Georgia", "serif"],
        sans: ["var(--font-inter)", "Be Vietnam Pro", "Inter", "system-ui", "sans-serif"],
        zen: ["var(--font-zen)", "cursive", "serif"]
      },
      borderRadius: {
        "zen-sm": "12px",
        "zen": "18px",
        "zen-lg": "24px",
        "zen-xl": "32px"
      },
      boxShadow: {
        "zen-subtle": "0 2px 8px -2px rgba(47, 58, 50, 0.05), 0 4px 16px -4px rgba(47, 58, 50, 0.04)",
        "zen-card": "0 4px 20px -4px rgba(79, 111, 82, 0.08), 0 2px 6px -2px rgba(79, 111, 82, 0.04)",
        "zen-floating": "0 12px 36px -8px rgba(79, 111, 82, 0.15)"
      },
      animation: {
        "pulse-slow": "pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite",
        "breathe": "breathe 12s ease-in-out infinite",
        "float": "float 6s ease-in-out infinite",
      },
      keyframes: {
        breathe: {
          "0%, 100%": { transform: "scale(1)", opacity: "0.8" },
          "33%": { transform: "scale(1.35)", opacity: "1" },
          "66%": { transform: "scale(1.35)", opacity: "0.9" }
        },
        float: {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-6px)" }
        }
      }
    },
  },
  plugins: [],
};
export default config;
