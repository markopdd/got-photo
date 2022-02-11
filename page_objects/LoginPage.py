from page_objects.BaseApp import BasePage


class LoginPage(BasePage):
    """Define login locators constants"""
    SELECT_LANGUAGE = '//*[@id="language-selector"]'
    CODE_FIELD = '//*[@id="accessCode"]'
    WRONG_CODE_MESSAGE = '//*[@class="ant-alert-message"]'
