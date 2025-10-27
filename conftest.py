# conftest.py
import pytest
from appium import webdriver
from utils.driver_manager import DriverManager

@pytest.fixture(scope="function")
def app_driver():
    """创建并返回 Appium 驱动实例（自动清理）"""
    driver = DriverManager.get_driver()
    yield driver  # 测试执行时提供 driver
    DriverManager.quit_driver(driver)  # 测试结束后自动清理