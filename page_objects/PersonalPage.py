from page_objects.BaseApp import BasePage


class PersonalPage(BasePage):
    """Define locators constants"""
    PAGE_TITTLE = '//*[text()="Personal information"]'
    FIRSTNAME = '//*[@id="firstname"]'
    LASTNAME = '//*[@id="lastname"]'
    EMAIL = '//*[@id="email"]'
    LOGIN_BUTTON = '//button/span[text()="Login"]'