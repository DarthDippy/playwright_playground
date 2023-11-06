from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cnn.com/politics")
    page.get_by_role("link", name="SCOTUS", exact=True).click()
    page.get_by_role("link", name="Congress", exact=True).click()
    page.get_by_role("link", name="Facts First", exact=True).click()
    page.get_by_role("link", name="Business Tech").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)