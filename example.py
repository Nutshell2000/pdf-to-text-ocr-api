# Run: pip install apify-client && APIFY_TOKEN=... python example.py
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
