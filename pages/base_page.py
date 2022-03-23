# -*- coding: utf-8 -*-

from typing import Type, Optional

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from constants import BASE_URL, MAXIMIZE, PAGE_TIMEOUT, IMPLICIT_WAIT, EXPLICIT_WAIT


class Page:
    """ Some abstract page for inheritance or direct non-context methods usage """

    def __init__(self, driver: WebDriver):
        super().__init__()
        self.driver = driver  # Required
        self.base_url = BASE_URL

        # options
        self.driver.set_page_load_timeout(PAGE_TIMEOUT)
        if MAXIMIZE:
            self.driver.maximize_window()
        if IMPLICIT_WAIT > 0:
            self.driver.implicitly_wait(IMPLICIT_WAIT)
        else:
            self.driver.implicitly_wait(0)

    def error_exists(self, by, locator) -> Optional[str]:
        try:
            elem = self._find((by, locator), ec.presence_of_element_located, timeout=2)
            if elem.is_displayed():
                return elem.text
        except (NoSuchElementException, TimeoutException):
            return None

    def get_url(self):
        return self.driver.current_url

    def is_visible(self, by, locator) -> bool:
        element = self._find((by, locator))
        return element.is_enabled() and element.is_displayed()

    def _open(self, path: str):
        self.driver.get(self.base_url + path if path.startswith('/') else '/' + path)

    def _find(self, elem: tuple[str, str], wait_reference: Type = ec.element_to_be_clickable, timeout=0) -> WebElement:
        if IMPLICIT_WAIT > 0:
            return self.driver.find_element(*elem)
        return WebDriverWait(self.driver, timeout or EXPLICIT_WAIT).until(wait_reference((elem[0], elem[1])))

    def _input(self, elem, text):
        elem = self._find(elem)
        elem.click()
        elem.clear()
        elem.send_keys(text)
