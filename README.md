# PDF to Text API with OCR for scanned PDFs

Send PDF links, get back clean text per document or per page, metadata, and OCR for scanned pages only (12 languages). Pages that already have text are never OCRed or charged for OCR.

This repo is a working example of calling the [PDF to Text API with OCR for scanned PDFs](https://apify.com/spellzcode/pdf-to-text-extractor) Apify actor from Node.js, Python, or without code. The actor runs on Apify's cloud; you pay per result and Apify's free plan includes $5 of monthly credit.

Made by SpellzCode, who also run the actor. Not affiliated with any site named here.

## What people use it for

- Feed PDFs into search, RAG or an LLM without silent empty pages
- Extract text from scanned contracts and invoices
- Get page-numbered text for citations

## Quick start without code

1. Open **[the actor on Apify](https://apify.com/spellzcode/pdf-to-text-extractor)** and sign in (free).
2. Paste your inputs, press **Start**.
3. Download the results as CSV, Excel or JSON, or connect them to Google Sheets, Make, Zapier or n8n.

## Quick start with code

Get an API token at [console.apify.com/settings/integrations](https://console.apify.com/settings/integrations), then:

```bash
git clone https://github.com/Nutshell2000/pdf-to-text-ocr-api.git
cd pdf-to-text-ocr-api
npm install
APIFY_TOKEN=your_token node example.mjs
```

Node.js ([example.mjs](example.mjs)):

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
  "pdfUrls": [
    "https://arxiv.org/pdf/1706.03762"
  ],
  "includePages": true,
  "ocrScanned": true,
  "ocrLanguage": "eng",
  "maxOcrPages": 50
};

const run = await client.actor('spellzcode/pdf-to-text-extractor').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const d of items) console.log(d.status, d.pageCount, d.looksScanned, (d.text ?? '').slice(0, 120));
```

Python ([example.py](example.py)):

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "pdfUrls": [
        "https://arxiv.org/pdf/1706.03762"
    ],
    "includePages": True,
    "ocrScanned": True,
    "ocrLanguage": "eng",
    "maxOcrPages": 50
}

run = client.actor("spellzcode/pdf-to-text-extractor").call(run_input=run_input)
for d in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(d.get('status'), d.get('pageCount'), d.get('looksScanned'), (d.get('text') or '')[:120])
```

## Input

```json
{
  "pdfUrls": [
    "https://arxiv.org/pdf/1706.03762"
  ],
  "includePages": true,
  "ocrScanned": true,
  "ocrLanguage": "eng",
  "maxOcrPages": 50
}
```

All fields are described on the actor's **Input** tab.

## Output (one row)

```json
{
  "url": "https://arxiv.org/pdf/1706.03762",
  "status": "ok",
  "pageCount": 15,
  "wordCount": 6462,
  "looksScanned": false,
  "ocrPageCount": 0,
  "ocrConfidence": null,
  "title": "Attention Is All You Need",
  "text": "Attention Is All You Need\n..."
}
```

## Price

$5 per 1,000 PDFs, plus $8 per 1,000 pages that needed OCR. Apify's paid plans get 10% to 30% off. Each run also has Apify's standard $0.00005 start charge.

## Limits

- OCR renders pages at 300 dpi with Tesseract. Clean print is read reliably; check figures where they matter, and treat a low `ocrConfidence` as a warning.
- Not for handwriting or angled phone photos.

## Guide

A longer walk-through: [your pdf to text pipeline is silently returning empty pages detecting scanned pdfs and when ocr is](https://dev.to/spellzcode/your-pdf-to-text-pipeline-is-silently-returning-empty-pages-detecting-scanned-pdfs-and-when-ocr-is-40d4)

## More tools

[All SpellzCode Apify actors](https://github.com/Nutshell2000/spellzcode-apify-actors): LinkedIn, TikTok and Threads profiles, company registers, contact details, email cleaning, PDFs, jobs, reviews and SEO.

## License

The example code in this repo is MIT licensed.
