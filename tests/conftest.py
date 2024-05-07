import os
from datetime import datetime

import pytest
from selenium import webdriver



@pytest.fixture()
def setup():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_directory = r'C:/Users/maheshpriya.j/PycharmProjects/Automation_Nasba_Store/Reports'

    if not os.path.exists(report_directory):
        os.makedirs(report_directory)

    config.option.htmlpath = os.path.join(
        report_directory,
        datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    )

