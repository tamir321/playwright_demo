from playwright.sync_api import sync_playwright

#PWDEBUG=1
#playwright show-trace trace.zip


with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("http://playwright.dev")
    page.get_by_role("link", name="Docs").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="GitHub repository").click()
    page1 = page1_info.value
    print(page.title())
    print(page1.title())
    context.tracing.stop(path="trace.zip")
    browser.close()

