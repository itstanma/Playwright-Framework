class verticals:
    def __init__ (self,page):
    
     self.page=page

    #verticals

     self.vertical=page.locator ('(//a[text()="Verticals"])[1]')
    

    #trading
     self.trade=page.locator('//strong[text()="Trading"]')

     self.trade1=page.locator('(//a[text()="Stock Trading"])[1]')
     self.trade2=page.locator('(//a[text()="Paper Trading"])[1]')
     self.trade3=page.locator('(//a[text()="CFD Trading"])[1]')
     self.trade4=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
     self.trade5=page.locator('(//a[text()="Algo Trading"])[1]')
     self.trade6=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
     self.trade7=page.locator('(//a[text()="Web Portal Trading"])[1]')

     self.trade_list=[self.trade1, self.trade2, self.trade3, self.trade4, self.trade5, self.trade6, self.trade7]


    #retail
     self.retail=page.locator('//strong[text()="Retail and Ecommerce"]')
     self.re1=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
     self.re2=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

     self.retail_list=[self.re1, self.re2]

    #health
     self.health=page.locator('//strong[text()="Healthcare"]')
     self.health1=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
     self.health2=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

     self.health_list=[self.health1, self.health2]

    #fintech
     self.fintech=page.locator('//strong[text()="Fintech"]')
     self.fintech1=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
     self.fintech2=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

     self.fintech_list=[self.fintech1, self.fintech2]

    #custom
     self.customapp=page.locator('//strong[text()="Custom App"]')
     self.cust1=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
     self.cust2=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
     self.cust3=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
     self.cust4=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
     self.cust5=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
     self.cust6=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
     self.cust7=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
     self.cust8=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
     self.cust9=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')

     self.customapp_list=[self.cust1,self.cust2,self.cust3, self.cust4, self.cust5, self.cust6, self.cust7, self.cust8,self.cust9]

    def click_trade_option(self):

     for i in self.trade_list:
        self.vertical.hover()
        self.trade.hover()
        i.click()
        self.page.wait_for_load_state('load')
        self.page.go_back()

    def click_retail_option(self):

     for i in self.retail_list:
        self.vertical.hover()
        self.retail.hover()
        i.click()
        self.page.wait_for_load_state('load')
        self.page.go_back()

    def click_health_option(self):  
       
       for i in self.health_list:
         self.vertical.hover()
         self.health.hover()
         i.click()
         self.page.wait_for_load_state('load')
         self.page.go_back()
    def click_fintech_option(self):

        for i in self.fintech_list:
          self.vertical.hover()
          self.fintech.hover()
          i.click()
          self.page.wait_for_load_state('load')
          self.page.go_back()
    def click_customapp_option(self):
      
         for i in self.customapp_list:
            self.vertical.hover()
            self.customapp.hover()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()




          


    



      




         




