import type { Metadata, Viewport } from "next";
import "./globals.css";
import { LanguageProvider } from "@/context/LanguageContext";
import { SoundProvider } from "@/context/SoundContext";
import { AuthProvider } from "@/context/AuthContext";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import MobileNav from "@/components/MobileNav";

export const metadata: Metadata = {
  title: "Học Coaching - Từ nền tảng khai vấn đến luyện thi ICF Credentialing",
  description:
    "Học Coaching cùng Coach Thanh Huyền - Nền tảng học khai vấn và luyện thi ICF Credentialing (ACC/PCC) chuẩn quốc tế 2025, phong cách Zen chánh niệm tĩnh tại.",
  manifest: "/manifest.json",
  openGraph: {
    title: "Học Coaching — Cùng Coach Thanh Huyền",
    description: "Từ nền tảng khai vấn đến luyện thi ICF Credentialing. Hiểu sâu chuẩn mực — Vững vàng phán đoán — Phát triển năng lực coaching.",
    type: "website",
    locale: "vi_VN"
  }
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
  themeColor: "#4F6F52"
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="vi" suppressHydrationWarning>
      <head>
        <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🪷</text></svg>" />
      </head>
      <body className="antialiased min-h-screen flex flex-col bg-zen-bg text-zen-ink">
        <LanguageProvider>
          <SoundProvider>
            <AuthProvider>
              <Header />
              <main className="flex-1 pb-20 md:pb-12">{children}</main>
              <Footer />
              <MobileNav />
            </AuthProvider>
          </SoundProvider>
        </LanguageProvider>

        {/* PWA Service Worker Registration */}
        <script
          dangerouslySetInnerHTML={{
            __html: `
              if ('serviceWorker' in navigator) {
                window.addEventListener('load', function() {
                  navigator.serviceWorker.register('/sw.js').catch(function(err) {
                    console.log('SW registration skipped:', err);
                  });
                });
              }
            `
          }}
        />
      </body>
    </html>
  );
}
