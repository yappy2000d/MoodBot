import { defineConfig } from "vitepress";

export const zh = defineConfig({
  lang: "zh-tw",

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [{ text: "首頁", link: "/zh" }],
    sidebar: [
      { text: "基本介紹", link: "/zh/intro" },
      { text: "前置準備", link: "/zh/setup" },
      {
        text: "LINE機器人",
        items: [
          { text: "覆誦機器人", link: "/zh/line" },
          { text: "自訂訊息", link: "/zh/line/msg" },
        ],
      },
      {
        text: "情緒分析",
        items: [
          { text: "數學原理", link: "/zh/ai/principle" },
          { text: "建立模型", link: "/zh/ai/build" },
        ],
      },
      { text: "影片爬蟲", link: "/zh/yt" }
    ],

    docFooter: {
      prev: "上一頁",
      next: "下一頁",
    },

    outline: {
      label: "頁面導覽",
    },

    lastUpdated: {
      text: "最后更新於",
      formatOptions: {
        dateStyle: "short",
        timeStyle: "medium",
      },
    },

    langMenuLabel: "多國语言",
    returnToTopLabel: "返回頂部",
    sidebarMenuLabel: "菜单",
    darkModeSwitchLabel: "主題",
    lightModeSwitchTitle: "切換至淺色模式",
    darkModeSwitchTitle: "切換到深色模式",
  },
});
