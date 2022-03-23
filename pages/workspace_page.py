# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.base_page import Page


class WorkspacePage(Page):

    email_input = By.CSS_SELECTOR, '#email-address'
    password_input = By.CSS_SELECTOR, '#password'
    error_box = By.XPATH, '//div[@data-testid="error-box"]'
    submit_button = By.CSS_SELECTOR, 'button[name=login-button]'

    def open_ws_url(self, ws_name):
        self._open(f'/workspace/{ws_name}/login')

    def input_login(self, login):
        self._input(self.email_input, login)

    def input_password(self, password):
        self._input(self.password_input, password)

    def submit(self):
        self._find(self.submit_button).click()



