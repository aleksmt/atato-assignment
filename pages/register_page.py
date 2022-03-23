# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import Page


class RegisterPage(Page):
    first_name_input = By.ID, 'firstname'
    last_name_input = By.ID, 'lastname'
    email_input = By.ID, 'email'
    workspace_name_input = By.ID, 'workspace'
    password_input = By.CSS_SELECTOR, 'input[name=password]'
    confirm_password_input = By.CSS_SELECTOR, 'input[name=confirm-password]'
    terms_and_conditions_link = By.CSS_SELECTOR, 'a[data-testid=terms]'
    privacy_policy_link = By.CSS_SELECTOR, 'a[data-testid=policy]'
    recaptcha_link = By.XPATH, '//iframe[@title="reCAPTCHA"]'

    agree_checkbox_tc = By.XPATH, '//input[@type="checkbox"]/ancestor::label[1]'
    register_button = By.XPATH, '//button[@name="register-button"]'
    login_link = By.CSS_SELECTOR, 'a[data-testid=login]'

    tc_error = By.CSS_SELECTOR, 'p[data-testid="terms-error"]'
    password_error = By.CSS_SELECTOR, 'div[name=popover-password]'  # ? check visible
    workspace_error = By.CSS_SELECTOR, '#workspace-feedback'
    submit_errors = By.CSS_SELECTOR, 'div[as=ui]'

    def open_register_url(self):
        self._open('/register')

    def set_first_name(self, text):
        self._input(self.first_name_input, text)

    def set_last_name(self, text):
        self._input(self.last_name_input, text)

    def set_email(self, text):
        self._input(self.email_input, text)

    def set_password(self, text):
        self._input(self.password_input, text)

    def set_password_confirmation(self, text):
        self._input(self.confirm_password_input, text)

    def set_both_passwords(self, text):
        self._input(self.password_input, text)
        self._input(self.confirm_password_input, text)

    def click_checkbox_tc(self):
        elem = self._find(self.agree_checkbox_tc, ec.presence_of_element_located)
        elem.click()

    def click_submit(self):
        elem = self._find(self.register_button)
        elem.click()

    def set_workspace(self, text):
        self._input(self.workspace_name_input, text)

    def clean_all_inputs(self):
        checkbox = self._find(self.agree_checkbox_tc, ec.presence_of_element_located)
        if checkbox.get_attribute('data-checked'):
            checkbox.click()
        self.set_first_name('')
        self.set_last_name('')
        self.set_email('\b' * 30)
        self.set_workspace('\b' * 30)
        self.set_password('')
        self.set_password_confirmation('')

    def open_tc(self):
        elem = self._find(self.terms_and_conditions_link)
        elem.click()

    def open_policy(self):
        elem = self._find(self.privacy_policy_link)
        elem.click()


