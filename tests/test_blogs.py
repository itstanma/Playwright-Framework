


import pytest

from pages.blogs import blog

@pytest.mark.smoke
def test_blogs(page):
 blogg=blog(page)
 blogg.click_blog_option()
