class blog:
    def __init__ (self,page):
    
     self.page=page

     self.blog=page.locator('(//a[text()="Blog"])[1]').click()

     self.app=page.locator('//a[@href="/blog/category/app-development/"]')

     self.web=page.locator('//a[@href="/blog/category/web-development/"]')
     self.software=page.locator('//a[@href="/blog/category/software-development/"]')
     self.digital=page.locator('//a[@href="/blog/category/digital-marketing/"]')
     self.email=page.locator('//a[@href="/blog/category/email-marketing/"]')
     self.artificial=page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
     self.ui=page.locator('//a[@href="/blog/category/ui-ux-design/"]')

     self.blog_list=[self.web,self.software, self.digital, self.email, self.artificial, self.ui ]

    def click_blog_option(self):

        for i in self.blog_list:
           i.click()
           self.page.wait_for_load_state('load')
           self.page.go_back()



