import type { Metadata, Viewport } from "next";
import "./globals.css";
import { LanguageProvider } from "@/context/LanguageContext";
import { SoundProvider } from "@/context/SoundContext";
import { AuthProvider } from "@/context/AuthContext";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import MobileNav from "@/components/MobileNav";

export const metadata: Metadata = {
  title: "Mentor thi ICF PCC - Luyện thi chứng chỉ ICF chuẩn quốc tế",
  description:
    "Ứng dụng luyện thi chứng chỉ ICF PCC song ngữ Anh - Việt, phong cách Zen chánh niệm tĩnh lặng, đầy đủ lý thuyết, từ khóa, flashcard, case study, quiz và đề thi thử phán đoán tình huống.",
  manifest: "/manifest.json"
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
