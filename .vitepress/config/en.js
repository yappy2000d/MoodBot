import { defineConfig } from "vitepress";

export const en = defineConfig({
  lang: "en",
  description: "An LINE Bot for Evaluating YouTube Video Comments",

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [{ text: "Home", link: "/" }],

    socialLinks: [
      { icon: "github", link: "https://github.com/yappy2000d/MoodBot" },
    ],
  },
});
