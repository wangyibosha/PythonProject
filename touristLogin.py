import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
# import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:


    def test_tourist_login(self,app_driver):
        """游客登录"""

        el1 = app_driver.find_element(AppiumBy.ID, 'com.homily.teach:id/agree_disclaimers_btn')
        el1.click()
        el2 = app_driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="游客模式登录"]')
        el2.click()

