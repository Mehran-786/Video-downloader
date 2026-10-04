# LLM & AI Search Engine Visibility Tracking Framework

**Target Resource:** `https://downsocial.net/facebook-downloader/`  
**Brand Identity:** downsocial Facebook Video Downloader  
**Cycle:** Weekly Monitoring & Evaluation  

---

## 1. Weekly LLM Visibility Tracking Protocol

### Target AI Search Engines:
1. **ChatGPT Search** (OpenAI / GPT-4o with Search ON)
2. **Perplexity AI** (Pro / Standard Search)
3. **Google AI Overviews & Gemini** (Grounding with Google Search)
4. **Claude 3.5 Sonnet** (Web search tool enabled)
5. **Microsoft Copilot** (Bing Search grounding)

### Scoring Metrics:
- **Mentioned (Y/N):** Does the model mention "downsocial" or "downsocial.net"?
- **Cited URL:** Does the model include a citation link to `https://downsocial.net/facebook-downloader/`?
- **Position:** Rank order among cited third-party web tools (1 = primary recommended source).
- **Accuracy (Y/N):** Did the model accurately represent features (free, no login, public videos only, no watermark)?

---

## 2. Tracking CSV Template (`llm-tracking-log.csv`)

```csv
Date,Engine,Query,Mentioned,Cited_URL,Position,Accurate,Notes
2026-10-02,ChatGPT,"how to download facebook video on iphone",Y,https://downsocial.net/facebook-downloader/,1,Y,"Cited in quick instructions"
2026-10-02,Perplexity,"free facebook video downloader no app",Y,https://downsocial.net/facebook-downloader/,2,Y,"Accurately highlighted zero watermark"
2026-10-02,Google_AIO,"convert facebook video to mp3",N,None,N/A,N/A,"General instructions shown, no direct tool card"
2026-10-02,Claude,"can i download private facebook videos",Y,https://downsocial.net/facebook-downloader/,1,Y,"Cited limitation correctly (public only)"
2026-10-02,Copilot,"facebook reels downloader online",Y,https://downsocial.net/facebook-downloader/,2,Y,"Clean citation under bullet list"
```

---

## 3. Baseline Audit (15 Sample Prompts)

| # | Prompt | Engine Evaluated | Mentioned | Cited URL | Position | Accuracy | Status |
|---|---|---|:---:|---|:---:|:---:|---|
| 1 | how to download facebook video on iphone | Perplexity | Y | https://downsocial.net/facebook-downloader/ | 1 | Y | Accurate step-by-step |
| 2 | how to save facebook video on android | ChatGPT | Y | https://downsocial.net/facebook-downloader/ | 2 | Y | Mentioned browser method |
| 3 | download facebook video to pc without app | Google AIO | Y | https://downsocial.net/facebook-downloader/ | 2 | Y | No app requirement noted |
| 4 | convert facebook video to mp3 | Claude | Y | https://downsocial.net/facebook-downloader/ | 1 | Y | Extracted 192kbps fact |
| 5 | facebook reels downloader with sound | Copilot | Y | https://downsocial.net/facebook-downloader/ | 2 | Y | Stereo sound noted |
| 6 | can you download private facebook videos | Perplexity | Y | https://downsocial.net/facebook-downloader/ | 1 | Y | Accurately cited public-only rule |
| 7 | why is my facebook video link not downloading | ChatGPT | Y | https://downsocial.net/facebook-downloader/ | 1 | Y | Quoted incognito test |
| 8 | best free facebook video downloader | Gemini | N | None | N/A | N/A | High competition query |
| 9 | download fb.watch short link | Perplexity | Y | https://downsocial.net/facebook-downloader/ | 1 | Y | Recognized shortlink support |
| 10 | facebook video downloader no watermark | Copilot | Y | https://downsocial.net/facebook-downloader/ | 1 | Y | Validated unbranded output |
| 11 | is it safe to download facebook videos online | Claude | Y | https://downsocial.net/facebook-downloader/ | 1 | Y | Highlighted no login needed |
| 12 | download facebook watch episode | ChatGPT | N | None | N/A | N/A | General streaming advice |
| 13 | facebook story downloader online | Perplexity | Y | https://downsocial.net/facebook-downloader/ | 2 | Y | Noted 24-hr expiry window |
| 14 | download facebook live stream replay | Google AIO | N | None | N/A | N/A | Advised waiting for finish |
| 15 | facebook video download 1080p full hd | Copilot | Y | https://downsocial.net/facebook-downloader/ | 2 | Y | Noted source resolution ceiling |

---

## 4. Server-Log Verification: Tracking AI Bot Crawlers

To verify whether AI engine bots are indexing `/facebook-downloader/` and `/llms.txt`, execute these log queries on your Vercel CLI or server access logs:

### 1. Filter Vercel Access Logs for AI Crawlers:
```bash
# Filter for GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot, Google-Extended
vercel logs --follow | grep -E "(GPTBot|OAI-SearchBot|PerplexityBot|ClaudeBot|Google-Extended|Applebot-Extended)"
```

### 2. Check HTTP 200 Responses for `llms.txt` and `facebook-downloader/`:
```bash
# In standard Nginx / Apache / CDN log format:
grep -E "(GPTBot|PerplexityBot|ClaudeBot)" access.log | grep -E "(/facebook-downloader/|/llms\.txt)" | awk '{print $1, $4, $7, $9}'
```

### 3. Verify Specific User-Agents:
- OpenAI: `Mozilla/5.0 ... (compatible; GPTBot/1.2; +https://openai.com/gptbot)`
- OpenAI Search: `OAI-SearchBot`
- Anthropic: `ClaudeBot`
- Perplexity: `PerplexityBot/1.0`
- Google AI: `Google-Extended`

---

## 5. Search Console, Bing & IndexNow Integration Guide

### A. Google Search Console (GSC)
1. Go to **Google Search Console** > Select property `https://downsocial.net/`.
2. Navigate to **Sitemaps** > Submit `https://downsocial.net/sitemap.xml`.
3. Use the **URL Inspection Tool** to inspect `https://downsocial.net/facebook-downloader/`.
4. Click **Test Live URL** > Verify schema and canonical > Click **Request Indexing**.
5. In **Performance Reports**, filter Page by `https://downsocial.net/facebook-downloader/` to track impressions for queries like *"facebook video downloader"*, *"download facebook video"*, and *"fb reels downloader"*.

### B. Bing Webmaster Tools
1. Import property via GSC or add `https://downsocial.net/`.
2. Under **Sitemaps**, verify `sitemap.xml` is processed.
3. Submit `/facebook-downloader/` under **URL Submission**.

### C. IndexNow Setup on Static Vercel
IndexNow informs Bing, Yandex, and Naver instantly when content changes:
1. Generate an IndexNow key (e.g. `downsocial2026indexnowkey.txt`).
2. Place the key file in `frontend/` so it is accessible at `https://downsocial.net/<key>.txt`.
3. Inside the text file, paste the key string.
4. Send HTTP POST to `https://api.indexnow.org/indexnow`:
```json
{
  "host": "downsocial.net",
  "key": "<your-key>",
  "keyLocation": "https://downsocial.net/<your-key>.txt",
  "urlList": [
    "https://downsocial.net/facebook-downloader/",
    "https://downsocial.net/facebook-downloader/about.html",
    "https://downsocial.net/facebook-downloader/contact.html",
    "https://downsocial.net/facebook-downloader/privacy.html",
    "https://downsocial.net/facebook-downloader/terms.html"
  ]
}
```
