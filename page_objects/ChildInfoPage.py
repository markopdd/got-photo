from page_objects.BaseApp import BasePage


class ChildPage(BasePage):
    """Define locators constants"""
    PAGE_TITTLE = '//*[text()="Child information"]'
    RECORD_POPUP = '//*[text()="Record found"]'
    TEACHER = '//*[@id="teacher"]'
    GROUP = '//*[@id="group"]'
    ADD_CHILD_BUTTON = '//button/span[text()="Add child"]'
    CONFIRM_BUTTON = '//button/span[text()="Confirm and shop products"]'
    SHOP_PRODUCTS_BUTTON = '//button/span[text()="Shop products"]'
    USE_DATA_RECORDS_BUTTON = '//*[text()="No, use my data instead of record data"]'
