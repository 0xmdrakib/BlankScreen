import type { Metadata } from "next";
import "./globals.css";

const siteUrl = "https://blankscreen.rakibhq.xyz";

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: "BlankScreen — Let the screen go black",
  description:
    "A tiny Windows utility that covers every display with pure black while your background work keeps running.",
  alternates: { canonical: "/" },
  icons: { icon: "/logo.png", apple: "/logo.png" },
  openGraph: {
    type: "website",
    url: siteUrl,
    siteName: "BlankScreen",
    title: "Keep the work running. Let the screen go black.",
    description: "One tiny Windows utility. No install. One touch to return.",
    images: [{ url: "/og.png", width: 1728, height: 908, alt: "BlankScreen — Keep the work running. Let the screen go black." }],
  },
  twitter: {
    card: "summary_large_image",
    title: "BlankScreen",
    description: "Keep the work running. Let the screen go black.",
    images: ["/og.png"],
  },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
