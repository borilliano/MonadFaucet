import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--start-maximized'])
    page = await browser.newPage()
    await page.goto('https://faucet.monad.xyz/', {'waitUntil': 'networkidle2'})

    # Wait for the "Connect Wallet" button to appear
    await page.waitForSelector('button', timeout=20000)

    # Find and click the "Connect Wallet" button
    buttons = await page.querySelectorAll('button')
    for btn in buttons:
        label = await (await btn.getProperty('innerText')).jsonValue()
        if 'Connect Wallet' in label:
            await btn.click()
            print("Clicked Connect Wallet button.")
            break

    # Wait for a few seconds to allow manual wallet connection
    await page.waitFor(15_000)

    # (Optional) You could attempt to click the "Request" button after wallet is connected,
    # but this requires wallet automation which is not supported in Python.

    print("Please complete wallet connection and request manually in the opened browser window.")
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
