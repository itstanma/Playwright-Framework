






import pytest

from pages.social import socialmedia

@pytest.mark.smoke


def test_socialmedia(page):
    social=socialmedia(page)
    social.social_click_option()