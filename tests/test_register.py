# -*- coding: utf-8 -*-

import time

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import Page
from pages.register_page import RegisterPage


def test_register_failure_1(driver: WebDriver):
    """ Block register if invalid inputs 1 """
    # initiating page objects
    register_page = RegisterPage(driver)
    register_page.open_register_url()

    # scenario 1
    assert register_page.is_visible(*register_page.first_name_input), 'login input is not visible'
    assert register_page.is_visible(*register_page.last_name_input), 'password input is not visible'
    assert register_page.is_visible(*register_page.email_input), 'email input is not visible'
    assert register_page.is_visible(*register_page.workspace_name_input), 'workspace input is not visible'
    assert register_page.is_visible(*register_page.password_input), 'password input is not visible'
    assert register_page.is_visible(*register_page.terms_and_conditions_link), 't&c link is not visible'
    assert register_page.is_visible(*register_page.recaptcha_link), 'google`s captcha is not visible'


def test_register_failure_2(driver: WebDriver):
    """ Block register if invalid inputs 2 """
    # initiating page objects
    register_page = RegisterPage(driver)
    register_page.open_register_url()

    # scenario 2
    register_page.set_first_name(f'first-{int(time.time())}')
    register_page.set_last_name(f'last-{int(time.time())}')
    register_page.set_email(f'foo-{int(time.time())}@bar.com')

    assert_no_errors(register_page)


@pytest.mark.skip(reason='Looks like scenario 2-1-1 is no longer valid, so it will be ignored')
def test_register_failure_2_1_1(driver: WebDriver):
    """ Block register if invalid inputs 2-1-1 """
    pass


def test_register_failure_2_1_2(driver: WebDriver):
    """ Block register if invalid inputs 2-1-2 """
    # initiating page objects
    register_page = RegisterPage(driver)
    register_page.open_register_url()

    # scenario 2-1-2 -> we cannot check error without actual data in input
    register_page.set_first_name(f'first-{int(time.time())}')
    register_page.set_last_name(f'last-{int(time.time())}')
    register_page.set_email(f'foo-{int(time.time())}@bar.com')

    register_page.set_workspace(f'workspace-*-{int(time.time())}')
    register_page.set_both_passwords('ASDASDSADqweqweqwe123123123!!')
    register_page.click_checkbox_tc()
    register_page.click_submit()
    assert register_page.error_exists(*register_page.workspace_error)


def test_register_failure_2_2(driver: WebDriver):
    """ Block register if invalid inputs 2-2 """
    # initiating page objects
    register_page = RegisterPage(driver)
    register_page.open_register_url()

    # scenario 2-2 -> we cannot check errors without proper data input
    register_page.set_first_name(f'first-{int(time.time())}')
    register_page.set_last_name(f'last-{int(time.time())}')
    register_page.set_email(f'foo-{int(time.time())}@bar.com')
    register_page.set_workspace(f'workspace-{int(time.time())}')

    register_page.set_both_passwords('less_ten')
    register_page.click_checkbox_tc()
    register_page.click_submit()

    assert 'At least 10 characters' in register_page.error_exists(*register_page.password_error)
    assert 'Requires a mixture of both' in register_page.error_exists(*register_page.password_error)
    assert 'Requires a mixture of letters and numbers' in register_page.error_exists(*register_page.password_error)
    assert 'Inclusion of at least one' in register_page.error_exists(*register_page.password_error)


##                                                                    ##
#  scenarios from 2-3 to 2-8 is missing, they're very similar. Sorry   #
##                                                                    ##


def test_legal_links(driver: WebDriver):
    """ Check Legal links """
    # initiating page objects
    register_page = RegisterPage(driver)
    page = Page(driver)
    register_page.open_register_url()

    main_window = driver.current_window_handle

    # scenario 1 -> there is no link to "use", so I've decided to leave only conditions
    register_page.open_tc()
    driver.switch_to.window(driver.window_handles[1])
    assert '/legal-terms-and-conditions' in page.get_url()
    driver.switch_to.window(main_window)

    # scenario 2
    register_page.open_policy()
    driver.switch_to.window(driver.window_handles[2])
    assert '/legal-privacy' in page.get_url()
    driver.switch_to.window(main_window)


def test_register_success(driver: WebDriver):
    """ Register success with valid inputs """
    # initiating page objects
    register_page = RegisterPage(driver)
    page = Page(driver)
    register_page.open_register_url()

    # scenario 2-2 -> we cannot check errors without proper data input
    register_page.set_first_name(f'first-{int(time.time())}')
    register_page.set_last_name(f'last-{int(time.time())}')
    register_page.set_email(f'foo-{int(time.time())}@bar.com')
    register_page.set_workspace(f'workspace-{int(time.time())}')

    register_page.set_both_passwords('ASDASDSADqweqweqwe123123123!!')
    register_page.click_checkbox_tc()
    register_page.click_submit()

    assert_no_errors(register_page)
    assert '/email-verification' in page.get_url()


def assert_no_errors(page: RegisterPage):
    assert not page.error_exists(*page.tc_error)
    assert not page.error_exists(*page.password_error)
    assert not page.error_exists(*page.workspace_error)
    assert not page.error_exists(*page.submit_errors)
