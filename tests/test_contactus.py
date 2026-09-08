import pytest

from pages.contactus import contact


@pytest.mark.smoke
def test_contactus(page):
	contact(page)
