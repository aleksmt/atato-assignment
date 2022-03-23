# -*- coding: utf-8 -*-

from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def change_base_dir(monkeypatch):
    monkeypatch.chdir(str(Path(__file__).parents[0]))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring
