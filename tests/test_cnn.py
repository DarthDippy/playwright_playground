from playwright.sync_api import Playwright, sync_playwright, expect
import re

def check_nav_bar(page) -> None:
    page.get_by_role("link", name="SCOTUS", exact=True).click()
    page.get_by_role("link", name="Congress", exact=True).click()
    page.get_by_role("link", name="Facts First", exact=True).click()
    page.get_by_role("link", name="Business Tech").click()
    
    expect(page).to_have_title(re.compile(r".*Tech | CNN Business"))
    #return "Tech | CNN Business"

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cnn.com/politics")
    check_nav_bar(page)
    #assert title == "123Tech | CNN Business"
    #expect(page).to_have_title(re.compile(r".*Tech"))
    #expect(page.to_have_title(), "Tech | CNN Business")
    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)