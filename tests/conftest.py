# -*- coding: utf-8 -*-

import logging
import tempfile

import pytest
from autoselenium import Driver

from constants import HEADLESS_MODE, BROWSER, IMPLICIT_WAIT, EXPLICIT_WAIT


@pytest.fixture(scope='session', autouse=True)
def initial_check():
    if IMPLICIT_WAIT > 0 and EXPLICIT_WAIT > 0:
        pytest.fail('Mixing of implicit/explicit waits is a bad practice!', False)
    if IMPLICIT_WAIT > 0:
        logging.info('Using waits implicitly')
    if EXPLICIT_WAIT > 0:
        logging.info('Using waits explicitly')


@pytest.fixture(scope='function')
def driver():
    wrapper = Driver(browser=BROWSER,
                     root=tempfile.gettempdir(),
                     headless=HEADLESS_MODE)
    yield wrapper.driver
    wrapper.quit()
