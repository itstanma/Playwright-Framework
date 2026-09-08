class contact:
    def __init__(self, page):
        self.page = page

        self.contactus = page.locator('(//a[text()="Contact us"])[1]')
        self.contactus.click()
        page.locator('(//input[@name="name"])[2]').fill('tanmaya')
        page.locator('(//input[@placeholder="Your Mail"])[2]').fill('tanmaya@gmail.com')
        page.once("dialog", lambda dialog: dialog.accept())
        page.locator('(//button[text()="Send OTP"])[2]').click()
        page.locator('(//input[@placeholder="Enter OTP"])[2]').fill('1234')
        page.locator('(//input[@placeholder="Your Company"])[2]').fill('abc')
        page.locator('(//select[@name="service"])[2]').select_option('Web Development')
        page.locator('(//input[@placeholder="Your Phone"])[2]').fill('1324321234')
        page.locator('(//textarea[@placeholder="Message"])[2]').fill('hi')
     