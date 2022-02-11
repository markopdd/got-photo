import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture()
def check_language():
    def run(page_object: object, language_field_selector: str, language: str,
                           tittle_selector: str, tittle: str) -> object:
        page_object.find_and_click(language_field_selector)
        page_object.select_text_option(language_field_selector, language)
        page_object.driver.refresh()
        return page_object.find_text_element(tittle_selector, tittle)
    return run
