# utils/driver_manager.py
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DriverManager:
    @staticmethod
    def get_driver():
        """创建并返回 Appium WebDriver 实例"""
        desired_caps = {
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
        try:
            self.driver = webdriver.Remote(
            "http://127.0.0.1:4723",
            options=UiAutomator2Options().load_capabilities(caps)
            )
        except Exception as e:
            print(f"初始化失败:{e}")
            exit(1)

    @staticmethod
    def quit_driver(driver):
        """安全关闭 WebDriver"""
        if driver:
            try:
                driver.quit()
            except Exception:
                pass  # 忽略关闭异常