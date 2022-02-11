from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """Define base locators constants"""
    MENU_BURGER = '//*[@aria-label="menu"]'
    CART = '//*[@aria-label="shopping-cart"]'
    CART_MESSAGE = '//*[@class="ant-popover-title"]'
    HELLO = '//h2[contains(text(), "Hello")]'
    LOGIN_BUTTON = '//*[text()="Login"]'
    LOGOUT_BUTTON = '//*[contains(text(), "Log out")]'

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    """Base methods"""
    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_and_click(self, xpath: str) -> object:
        return self.driver.find_element(By.XPATH, xpath).click()

    def send_data(self, xpath: str, keys: str) -> object:
        return self.driver.find_element(By.XPATH, xpath).send_keys(keys)

    def get_element_text(self, xpath: str) -> object:
        return self.driver.find_element(By.XPATH, xpath).text

    def open_menu(self):
        self.find_and_click(BasePage.MENU_BURGER)
        return self.find_text_element(BasePage.HELLO, "Hello")

    """Explicit wait methods"""
    def find_element(self, xpath: str, time: int = 10) -> object:
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located((By.XPATH, xpath)),
                                                      message=f"Can't find element by locator {xpath}")

    def find_clickable_element(self, xpath: str, time: int = 10) -> object:
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable((By.XPATH, xpath)),
                                                      message=f"Can't find element by locator {xpath}")

    def find_text_element(self, xpath: str, text: str, time: int = 10) -> object:
        return WebDriverWait(self.driver, time).until(ec.text_to_be_present_in_element((By.XPATH, xpath), text),
                                                      message=f"Can't find element by locator {xpath}")

    def select_text_option(self, locator: any, text: str) -> object:
        return Select(self.find_element(locator)).select_by_visible_text(text)
