






import pytest

from pages.vertical import verticals

@pytest.mark.smoke
def test_trading(page):
    trade=verticals(page)
    trade.click_trade_option()

def test_retail(page):
    retail=verticals(page)
    retail.click_retail_option()

def test_health(page):
    health=verticals(page)
    health.click_health_option()

def test_fintech(page):
    fintech=verticals(page)
    fintech.click_fintech_option()
    
def test_customapp(page):
    customapp=verticals(page)
    customapp.click_customapp_option()






