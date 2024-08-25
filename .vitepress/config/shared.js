import { defineConfig } from "vitepress";

export const shared = defineConfig({
  title: "MoodBot",

  themeConfig: {
    socialLinks: [
      { icon: "github", link: "https://github.com/yappy2000d/MoodBot" },
    ],
    footer: {
      message: "Released under the MIT License.",
      copyright: "Copyright © 2024-present yappy2000",
    },
  },
});
