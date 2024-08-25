import{_ as e,c as a,o as t,a2 as s}from"./chunks/framework.C94oF1kp.js";const r="/assets/setup_01.C9636yln.png",o="/assets/setup_02.CRNp804o.png",i="/assets/setup_03.D_FARj1g.png",n="/assets/setup_04.DLwQw_Kv.png",f=JSON.parse('{"title":"前置準備","description":"","frontmatter":{},"headers":[],"relativePath":"zh/setup.md","filePath":"zh/setup.md"}'),p={name:"zh/setup.md"},l=s('<h1 id="前置準備" tabindex="-1">前置準備 <a class="header-anchor" href="#前置準備" aria-label="Permalink to &quot;前置準備&quot;">​</a></h1><div class="important custom-block github-alert"><p class="custom-block-title">IMPORTANT</p><p>在開始之前，你需要一個LINE帳號。可以前往<a href="https://line.me/" target="_blank" rel="noreferrer">LINE 官網</a>並透過他們的APP申請一個帳號。</p></div><h2 id="官方帳號" tabindex="-1">官方帳號 <a class="header-anchor" href="#官方帳號" aria-label="Permalink to &quot;官方帳號&quot;">​</a></h2><p>我們得先為我們的機器人申請一個官方帳號。</p><p>首先登入<a href="https://manager.line.biz/" target="_blank" rel="noreferrer">LINE官方帳號管理頁面</a>，並建立一個新的帳號。</p><p>填寫相關資料後，可以進到這個畫面。 <img src="'+r+'" alt=""></p><p>進入設定 &gt; 回應設定。<br> 開啟Webhook並關閉自動回應訊息。 <img src="'+o+'" alt=""></p><h2 id="messaging-api" tabindex="-1">Messaging API <a class="header-anchor" href="#messaging-api" aria-label="Permalink to &quot;Messaging API&quot;">​</a></h2><p>登入<a href="https://developers.line.biz/console/" target="_blank" rel="noreferrer">LINE Developers</a>，建立一個Provider。</p><p>接著建立一個Messaging API <img src="'+i+'" alt=""></p><p>建立完成後的畫面長這樣 <img src="'+n+'" alt=""></p><p>請找到並保存好以下這兩個字串。我們之後會用到它們：</p><ol><li>在Basic settings頁面的Channel secret</li><li>在Messaging API頁面的Channel access token</li></ol><div class="tip custom-block github-alert"><p class="custom-block-title">TIP</p><p>如果沒有看到，可以按Issue按鈕來生成。</p></div><h2 id="webhook" tabindex="-1">Webhook <a class="header-anchor" href="#webhook" aria-label="Permalink to &quot;Webhook&quot;">​</a></h2><p>為了獲取Webhook URL，建議註冊一個<a href="https://ngrok.com/" target="_blank" rel="noreferrer">ngrok</a>帳號來方便開發。</p><hr><p>恭喜，現在一切已準備就緒，我們馬上來設計自己的機器人吧！</p>',18),c=[l];function h(_,g,d,m,u,b){return t(),a("div",null,c)}const P=e(p,[["render",h]]);export{f as __pageData,P as default};