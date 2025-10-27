import time
from telnetlib import EC

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

caps={
  "platformName": "Android",
  "appium:automationName": "uiautomator2",
  "appium:deviceName": "Q2NNW20728005993",
  "appium:appPackage": "com.homily.teach",
  "appium:appActivity": ".activity.SplashscreenActivity",
    "noReset":"false"
}

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=UiAutomator2Options().load_capabilities(caps)
)

#driver.find_element(AppiumBy.ACCESSIBILITY_ID,"弘历投教"),#connect_desc有值，这个定位方法才适用
driver.find_element(AppiumBy.ID,'com.homily.teach:id/agree_disclaimers_btn').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.homily.teach:id/select_account_login"]/android.widget.ImageView').click()
time.sleep(1)
el1 = driver.find_element(AppiumBy.ID,'com.homily.teach:id/mobile_phone_edit')
el1.send_keys("30017528")
el2 = driver.find_element(AppiumBy.ID,'com.homily.teach:id/password_edit')
el2.send_keys("679805__")
el2 = driver.find_element(AppiumBy.ID,'com.homily.teach:id/login_btn').click()
time.sleep(1)
driver.find_element(AppiumBy.ID,'com.homily.teach:id/confirm_btn').click()

