import pytest
import logging

from page_objects.LoginPage import LoginPage
from page_objects.PersonalPage import PersonalPage
from page_objects.ChildInfoPage import ChildPage
from page_objects.PhotoEventPage import EventPage

import test_data.data as td


def test_login_page_smoke(browser):
    """Test login page url is open and showing h1 "Welcome" tittle
    as default for English US website version"
    """
    login_main_page = LoginPage(browser, td.URL)
    login_main_page.go_to_site()
    assert login_main_page.find_text_element('//h1', td.TITTLES[0]), \
        logging.error(f'Can\'t open url {td.URL} or no {td.TITTLES[0]} tittle found')


def test_login_e2e(browser):
    """Test end to end login procedure and validate personal "Hello USER_TEST_DATA['firstname'] message!" """
    login_main_page = LoginPage(browser, td.URL)
    login_main_page.go_to_site()
    login_main_page.find_text_element('//h1', td.TITTLES[0])
    login_main_page.send_data(login_main_page.CODE_FIELD, td.USER_TEST_DATA['password'])
    login_main_page.find_and_click(login_main_page.LOGIN_BUTTON)

    # Forward to Personal Information Page
    personal_page = login_main_page
    assert personal_page.find_element(PersonalPage.PAGE_TITTLE), \
        logging.error(f'Can\'t forward to {PersonalPage.PAGE_TITTLE} web page')
    personal_page.send_data(PersonalPage.FIRSTNAME, td.USER_TEST_DATA['firstname'])
    personal_page.send_data(PersonalPage.LASTNAME, td.USER_TEST_DATA['lastname'])
    personal_page.send_data(PersonalPage.EMAIL, td.USER_TEST_DATA['email'])
    personal_page.find_and_click(PersonalPage.LOGIN_BUTTON)

    # Forward to Child Information Page
    child_info_page = personal_page
    assert child_info_page.find_element(ChildPage.PAGE_TITTLE), \
        logging.error(f'Can\'t forward to {ChildPage.PAGE_TITTLE} web page')
    child_info_page.send_data(PersonalPage.FIRSTNAME, td.USER_TEST_DATA['firstname'])
    child_info_page.send_data(PersonalPage.LASTNAME, td.USER_TEST_DATA['lastname'])
    child_info_page.send_data(ChildPage.TEACHER, td.USER_TEST_DATA['teacher'])
    child_info_page.send_data(ChildPage.GROUP, td.USER_TEST_DATA['group'])

    try:
        """ Let's try to add record data if there are records in base
        let's click "No" and continue with new data instead of recorded.
        """
        child_info_page.find_and_click(ChildPage.ADD_CHILD_BUTTON)
        if not personal_page.find_element(ChildPage.RECORD_POPUP):
            child_info_page.find_and_click(ChildPage.SHOP_PRODUCTS_BUTTON)
        else:
            logging.error("Error occurred! No data added or found.")
            pytest.fail()
    except Exception:
        child_info_page.find_and_click(ChildPage.USE_DATA_RECORDS_BUTTON)

    child_info_page.find_and_click(ChildPage.CONFIRM_BUTTON)

    # Forward to Event Page
    event_page = child_info_page
    assert event_page.find_element(EventPage.PAGE_TITTLE), \
        logging.error(f'Can\'t forward to {ChildPage.PAGE_TITTLE} web page')

    event_page.open_menu()
    check_user_hello = event_page.get_element_text(event_page.HELLO)
    assert check_user_hello == f"Hello {td.USER_TEST_DATA['firstname']}!", \
        logging.error(f"Assertion error! {check_user_hello} --> {td.USER_TEST_DATA['firstname']}!")

    event_page.find_clickable_element(event_page.LOGOUT_BUTTON)
    event_page.find_and_click(event_page.LOGOUT_BUTTON)


def test_login_page_language_tittles(browser):
    """Test login page showing correct h1 "Welcome"tittle relevant to chosen language
    """
    login_main_page = LoginPage(browser, td.URL)
    login_main_page.go_to_site()

    # Check English tittle as default
    assert login_main_page.find_text_element('//h1', td.TITTLES[0]), \
        logging.error(f'Tittle is not relevant {td.LANGUAGES[0]} --> {td.TITTLES[0]}')

    # Check Français tittle
    login_main_page.find_and_click(login_main_page.SELECT_LANGUAGE)
    login_main_page.select_text_option(login_main_page.SELECT_LANGUAGE, td.LANGUAGES[1])
    assert login_main_page.find_text_element('//h1', td.TITTLES[1]), \
        logging.error(f'Tittle is not relevant {td.LANGUAGES[1]} --> {td.TITTLES[1]}')

    # Check Español tittle
    login_main_page.find_and_click(login_main_page.SELECT_LANGUAGE)
    login_main_page.select_text_option(login_main_page.SELECT_LANGUAGE, td.LANGUAGES[2])
    assert login_main_page.find_text_element('//h1', td.TITTLES[2]), \
        logging.error(f'Tittle is not relevant {td.LANGUAGES[2]} --> {td.TITTLES[2]}')
