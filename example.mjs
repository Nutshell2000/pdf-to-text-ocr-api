// Run: npm install && APIFY_TOKEN=... node example.mjs
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
