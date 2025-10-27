import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
# import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def test_weixin_login(self):
        """微信登录"""

        try:
            el1 = self.driver.find_element(AppiumBy.ID, 'com.homily.teach:id/agree_disclaimers_btn')
            el1.click()
            print("重新开始")
        except Exception as e:
            time.sleep(2)
            el2 = self.driver.find_element(AppiumBy.XPATH,
                                     '//android.widget.LinearLayout[@resource-id="com.homily.teach:id/select_account_login"]/android.widget.ImageView')
            el2.click()
            print(f"")
