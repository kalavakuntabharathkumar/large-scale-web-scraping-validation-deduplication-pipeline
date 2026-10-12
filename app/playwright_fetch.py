from playwright.async_api import async_playwright

async def render(url):
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True)
        page=await browser.new_page()
        await page.goto(url,wait_until="networkidle")
        html=await page.content()
        await browser.close()
        return html
