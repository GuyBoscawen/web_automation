import pytest

from unittest.mock import MagicMock

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotInteractableException

import web_automation


def _get_headless_driver(_):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
    driver.implicitly_wait(10)
    return driver


@pytest.fixture(autouse=True)
def mock_webdriver(monkeypatch):
    monkeypatch.setattr(
        "webdriver_conf.get_webdriver",
        _get_headless_driver
    )


def test_web_automation_success():
    # This test navigates through the site in headless mode. Provided no exceptions are raised,
    # a successful navigation will return 'success'
    mock_args = MagicMock()
    site_navigation = web_automation._navigate_site(['chrome'])
    assert site_navigation == 'success'


def test_web_automation_failure(monkeypatch):
    mock_args = MagicMock()
    monkeypatch.setattr(
        'website_actions.nate._get_nate_start_page',
        lambda: "https://www.selenium.dev/"
    )
    with pytest.raises(ElementNotInteractableException):
        web_automation._navigate_site(['chrome'])
