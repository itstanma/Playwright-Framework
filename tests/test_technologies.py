




import pytest

from pages.technologies import technology


@pytest.mark.smoke
def test_ecom(page):
    ecom=technology(page)
    ecom.click_ecom_option()
    
def test_mobapp(page):
    mobapp=technology(page)
    mobapp.click_mobapp_option()

    

