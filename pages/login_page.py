from playwright.sync_api import Page

class loginPage:

    def __init__(self,page : Page):
        self.page = page
        self.email_txt = page.locator("#email")
        self.password_txt = page.locator('//*[@id = "passwd"]')
        self.submit_btn = page.locator('//*[@name = "SubmitLogin"]')

    def login(self,user,password):
        self.email_txt.fill(user)
        self.password_txt.fill(password)
        self.submit_btn.click()

