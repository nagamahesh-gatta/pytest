import pytest


@pytest.mark.usefixtures
def test_title(browser):
    browser.get('https://www.google.com')
    assert browser.title == 'Google'
