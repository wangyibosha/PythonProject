import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
# import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def setup_method(self):
        caps = {
            "platformName": "Android",
            "appium:automationName": "uiautomator2",
            "appium:deviceName": "Q2NNW20728005993",
            "appium:appPackage": "com.homily.teach",
            "appium:appActivity": ".activity.SplashscreenActivity",
            "appium.noReset": "true",
            # 添加这些关键的超时设置
            "appium:uiautomator2ServerLaunchTimeout":60000,
            "appium:uiautomator2ServerInstallTimeout": 60000,
            "appium:androidInstallTimeout": 120000,
            "appium:adbExecTimeout": 120000,
            "appium:newCommandTimeout": 300,
            "appium:autoGrantPermissions": True
        }
        # self.driver.implicitly_wait(10)
        '''
        显式等待
        '''
        #另一种写法
        # caps["appium:deviceName"] = "Q2NNW20728005993"
        try:
            self.driver = webdriver.Remote(
            "http://127.0.0.1:4723",
            options=UiAutomator2Options().load_capabilities(caps)
            )
        except Exception as e:
            print(f"初始化失败:{e}")
            exit(1)

        self.driver.implicitly_wait(10)#隐式等待

    def teardown(self):
        #打开新的APP self.driver.activate_app("包名")
        #关闭包 self.driver.terminate_app("包名")
        self.driver.quit()

    def test_tourist_login(self):
        """游客登录"""

        el1 = self.driver.find_element(AppiumBy.ID, 'com.homily.teach:id/agree_disclaimers_btn')
        el1.click()
        el2 = self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="游客模式登录"]')
        el2.click()
        result = self.driver.find_element(AppiumBy.ID,'com.homily.teach:id/tab_home')
        assert result.text == "首页"

    def test_normal_login(self):
        """账号密码登录"""
        self.driver.implicitly_wait(10)
        # driver.find_element(AppiumBy.ACCESSIBILITY_ID,"弘历投教"),#connect_desc有值，这个定位方法才适用
        el1 = self.driver.find_element(AppiumBy.ID, 'com.homily.teach:id/agree_disclaimers_btn')
        el1.click()
        time.sleep(2)
        self.driver.find_element(AppiumBy.XPATH,
                            '//android.widget.LinearLayout[@resource-id="com.homily.teach:id/select_account_login"]/android.widget.ImageView').click()
        time.sleep(3)
        el2 = self.driver.find_element(AppiumBy.ID, 'com.homily.teach:id/mobile_phone_edit')
        el2.send_keys("30017528")
        el3 = self.driver.find_element(AppiumBy.ID, 'com.homily.teach:id/password_edit')
        el3.send_keys("679805__")
        self.driver.find_element(AppiumBy.ID, 'com.homily.teach:id/login_btn').click()
        time.sleep(3)#强制等待
        self.driver.find_element(AppiumBy.ID, 'com.homily.teach:id/confirm_btn').click()
        result = self.driver.find_element(AppiumBy.ID,'com.homily.teach:id/tab_home')
        assert result.text == "首页"

    # def test_weixin_login(self):
    #     """微信登录"""
    #
    #     try:
    #         el1 = self.driver.find_element(AppiumBy.ID, 'com.homily.teach:id/agree_disclaimers_btn')
    #         el1.click()
    #         print("重新开始")
    #     except Exception as e:
    #         time.sleep(2)
    #         el2 = self.driver.find_element(AppiumBy.XPATH,
    #                                  '//android.widget.LinearLayout[@resource-id="com.homily.teach:id/select_account_login"]/android.widget.ImageView')
    #         el2.click()
    #         print(f"")
