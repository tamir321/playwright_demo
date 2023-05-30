from playwright.sync_api import sync_playwright
import pytest
from pages.main_page import mainPage
from pages.login_page import loginPage
@pytest.fixture
def _page(request):
    with sync_playwright() as playwright:
        playwright.selectors.set_test_id_attribute("my_project_uniq_id_attribute")  #page.get_by_test_id() to locate an element based on its data-testid attribute (other attributes can be configured).
        browser = playwright.chromium.launch()
        context = browser.new_context(ignore_https_errors=True,viewport={'width':1920,'height':1080})
        context.tracing.start(screenshots=True,snapshots=True,sources=True)
        page = context.new_page()
        yield page

        test_name = request.session.items[0].name

        if request.session.testsfailed:
            file_name = f"{test_name}.zip"
            context.tracing.stop(file_name)
        context.close()


def test_first_play_wright(_page):
    login_page = loginPage(_page)
    main_page = mainPage(_page)
    main_page.navigate()
    main_page.Sign_in_btn.click()
    login_page.login("test@sela.com","123456")


    #
    # page.get_by_role("button", name=" Sign in").click()
    # page.get_by_role("link", name=".  .").click()
    # page.locator("#email").click()
    # page.locator("#email").fill("1234")
    # page.get_by_label("Password").click()
    # page.get_by_label("Password").fill("4567")
    # page.get_by_role("button", name=" Sign in").click()