# Large-Scale Web Scraping, Validation and Deduplication Pipeline

Python pipeline demonstrating Scrapy collection, Playwright rendering, Pandas processing,
MinHash/LSH deduplication, validation, MongoDB/Docker infrastructure, and Cron scheduling.

## Run
python -m venv .venv
pip install -r requirements.txt
python -m playwright install chromium
docker compose up -d
scrapy crawl supplier

Process an exported CSV:
python app/process.py

Only crawl sites you are authorized to access and follow robots.txt, terms, and rate limits.

The resume metrics should only be presented as measured outcomes when backed by actual
run logs, datasets, and monitoring records.
