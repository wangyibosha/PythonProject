from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

caps={
  "platformName": "Android",
  "appium:automationName": "uiautomator2",
  "appium:deviceName": "emulator-5554",
  "appium:appPackage": "com.homilychart.zh",
  "appium:appActivity": ".activity.SplashActivity",
  "noReset":"true"
}

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=UiAutomator2Options().load_capabilities(caps)
)

el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="弘历锦囊")
el3.click()
el4 = driver.find_element(by=AppiumBy.ID, value="com.homilychart.zh:id/mobile_phone_edit")
el4.send_keys("30017528")
el5 = driver.find_element(by=AppiumBy.ID, value="com.homilychart.zh:id/password_edit")
el5.send_keys("679805__")
el6 = driver.find_element(by=AppiumBy.ID, value="com.homilychart.zh:id/login_btn")
el6.click()
el7 = driver.find_element(by=AppiumBy.ID, value="com.homilychart.zh:id/confirm_btn")
el7.click()
el8 = driver.find_element(by=AppiumBy.ID, value="com.homilychart.zh:id/no_update")
el8.click()
el9 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView")
el9.click()