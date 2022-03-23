# -*- coding: utf-8 -*-

from selenium.webdriver.remote.webdriver import WebDriver
from pages.workspace_page import WorkspacePage


def test_login_failed(driver: WebDriver):
    """ Login fail with invalid account """
    workspace_page = WorkspacePage(driver)

    workspace_page.open_ws_url('workspace')
    workspace_page.input_login('test@test.test')
    workspace_page.input_password('test')
    workspace_page.submit()

    assert workspace_page.error_exists(*workspace_page.error_box)
