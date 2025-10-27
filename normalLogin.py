import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
# import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def test_normal_login(self,app_driver):
        """账号密码登录"""
        app_driver.implicitly_wait(10)
        # driver.find_element(AppiumBy.ACCESSIBILITY_ID,"弘历投教"),#connect_desc有值，这个定位方法才适用
        el1 = app_driver.find_element(AppiumBy.ID, 'com.homily.teach:id/agree_disclaimers_btn')
        el1.click()
        time.sleep(2)
        app_driver.find_element(AppiumBy.XPATH,
                            '//android.widget.LinearLayout[@resource-id="com.homily.teach:id/select_account_login"]/android.widget.ImageView').click()
        time.sleep(3)
        el2 = app_driver.find_element(AppiumBy.ID, 'com.homily.teach:id/mobile_phone_edit')
        el2.send_keys("30017528")
        el3 = app_driver.find_element(AppiumBy.ID, 'com.homily.teach:id/password_edit')
        el3.send_keys("679805__")
        app_driver.find_element(AppiumBy.ID, 'com.homily.teach:id/login_btn').click()
        time.sleep(3)#强制等待
        app_driver.find_element(AppiumBy.ID, 'com.homily.teach:id/confirm_btn').click()
        result = app_driver.find_element(AppiumBy.ID,'com.homily.teach:id/tab_home')
        assert result.text == "首页"
