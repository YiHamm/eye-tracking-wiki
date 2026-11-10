# Eye Tracking Wiki — 眼動追蹤與視線估計

本專案包含 `index.html`（Wiki 網頁）、`sources.json`（五篇文獻的結構化摘要）與 `scripts/search_wiki.py`（關鍵字查詢工具）。

## 開始使用

1. 解壓縮專案，用瀏覽器開啟 `index.html`。
2. 在專案根目錄開啟 VS Code 終端機。
3. 執行 `python scripts/search_wiki.py`，輸入 `gaze`、`calibration` 或 `model`。
4. 也可以執行 `python scripts/search_wiki.py --query gaze` 直接查詢。

不需要安裝第三方 Python 套件。

## 資料與限制

`sources.json` 已收錄五篇文獻的來源網址、摘要與主題分類；這是結構化資料匯入的初步成果。此查詢程式是關鍵字比對，**尚非 LLM 語意檢索或 RAG**。如需證明完整的 LLM Wiki 流程，仍須加入 AI 查詢／生成與人工核對紀錄；文獻摘要也應以原文逐項驗證。
