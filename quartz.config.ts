import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "The Economic Archive" ,
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "quartz.jzhao.xyz",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Lora",
        body: "Inter",
        code: "Fira Code",
      },
      colors: {
        lightMode: {
          light: "#faf8f8", // Màu nền trắng ngà (đỡ chói)
          lightgray: "#e5e5e5", // Màu viền
          gray: "#b8b8b8", // Màu chữ phụ
          darkgray: "#4e4e4e", // Màu chữ chính (đọc siêu rõ)
          dark: "#2b2b2b", // Màu tiêu đề
          secondary: "#284b63", // Màu link (Xanh biển đậm sang trọng)
          tertiary: "#84a59d", // Màu hover
          highlight: "rgb(255, 255, 255)", // Màu highlight nền
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161920", // Nền "Hang động" cực tối
          lightgray: "#292d3e", // Viền và Graph view nhạt
          gray: "#7982a6", // Chữ phụ (ngày tháng, tag)
          darkgray: "#c3c7db", // Chữ nội dung (xám sáng dễ đọc)
          dark: "#ffffff", // Chữ tiêu đề (trắng muốt)
          secondary: "#82aaff", // Xanh dương sáng (giống màu H1 của ông)
          tertiary: "#c792ea", // Tím neon (giống màu H2 của ông)
          highlight: "rgba(130, 170, 255, 0.15)", // Bôi đen màu xanh nhạt
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
      Plugin.Citations({ bibliographyFile: "./content/bibliography.bib" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
