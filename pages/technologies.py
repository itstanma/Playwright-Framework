class technology:
    def __init__ (self,page):
    
     self.page=page
     #technology
     self.tech=page.locator('(//a[text()="Technologies"])[1]')
     #ecom
     self.ecom=page.locator('//strong[text()="eCommerce Development"]')

     self.ecom1=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
     self.ecom2=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
     self.ecom3=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
     self.ecom4=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
     self.ecom5=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
     self.ecom6=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
     self.ecom7=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
     self.ecom8=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
     self.ecom9=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
     self.ecom10=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
     self.ecom11=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
     self.ecom12=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
     self.ecom12=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
     self.ecom13=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
     self.ecom14=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
     self.ecom15=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
     self.ecom16=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')

     self.ecom_list=[self.ecom1, self.ecom2, self.ecom3,self.ecom4,self.ecom5,self.ecom6,self.ecom7,self.ecom8,self.ecom9,self.ecom10,self.ecom11,self.ecom12,self.ecom13,self.ecom14,self.ecom15,self.ecom16]

     #mobapp
     self.mobapp=page.locator('//strong[text()="Mobile App Development"]')

     self.mobapp1=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
     self.mobapp2=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
     self.mobapp3=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
     self.mobapp4=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
     self.mobapp5=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')

     self.mobapp_list=[self.mobapp1,self.mobapp2, self.mobapp3, self.mobapp4,self.mobapp5]

    def click_ecom_option(self):
       for i in self.ecom_list:
          self.tech.hover()
          self.ecom.hover()
          i.click()
          self.page.wait_for_load_state('load')
          self.page.go_back()

    def click_mobapp_option(self):
       for i in self.mobapp_list:
          self.tech.hover()
          self.mobapp.hover()
          i.click()
          self.page.wait_for_load_state('load')
          self.page.go_back()


          
            


           





