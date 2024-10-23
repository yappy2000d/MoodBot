import { defineConfig } from "vitepress";

export default defineConfig({
  base: "/MoodBot/",
  title: "MoodBot",

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [{ text: "首頁", link: "/" }],
    sidebar: [
      { text: "基本介紹", link: "/intro" },
      { text: "前置準備", link: "/setup" },
      {
        text: "LINE機器人",
        items: [
          { text: "覆誦機器人", link: "/line" },
          { text: "自訂訊息", link: "/line/msg" },
        ],
      },
      {
        text: "情緒分析",
        items: [
          { text: "數學原理", link: "/ai/principle" },
          { text: "建立模型", link: "/ai/build" },
        ],
      },
      { text: "影片爬蟲", link: "/yt" },
    ],

    socialLinks: [
      { icon: "github", link: "https://github.com/yappy2000d/MoodBot" },
    ],

    footer: {
      message: "Released under the MIT License.",
      copyright: "Copyright © 2024-present yappy2000",
    },
  },
});
