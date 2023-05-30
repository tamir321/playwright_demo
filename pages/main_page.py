from playwright.sync_api import Page

class mainPage:

    def __init__(self,page : Page):
        self.page = page
        self.Sign_in_btn = page.locator('.login')


    def navigate(self):
        self.page.goto("http://automationpractice.pl/index.php")


