class socialmedia:
    def __init__(self, page):
        self.page = page
        self.portfolio = page.locator('a[href*="portfolio"]').first
        self.social_list = [
            'https://www.facebook.com/TrankTechnologies',
            'https://in.linkedin.com/company/trank-technologies-official',
            'https://www.instagram.com/tranktechnologies/',
            'https://in.pinterest.com/tranktechnologies12/',
            'https://twitter.com/tranktechno',
            'https://www.youtube.com/channel/UCWu1Y-tfrXf-Utpaft830Cg',
            'https://www.quora.com/profile/Trank-Technologies-1',
        ]

    def social_click_option(self):
        self.portfolio.wait_for(state='visible', timeout=30000)
        self.portfolio.click()
        self.page.wait_for_load_state('load')

        for url in self.social_list:
            self.page.goto('https://www.tranktechnologies.com/portfolio', wait_until='load', timeout=120000)
            locator = self.page.locator(f'a[href="{url}"]')
            locator.wait_for(state='visible', timeout=30000)
            locator.first.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()
            self.page.wait_for_load_state('load')


