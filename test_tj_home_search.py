from appium.webdriver.common.appiumby import AppiumBy

import normalLogin
from normalLogin import TestLogin

class TestSearch:
    def test_search_home(self,app_driver):
        TestLogin.setup_method()
        s1 = app_driver.find.element(AppiumBy.ID,'com.homily.teach:id/stock_search')
        s1.click()



if __name__ == '__main__':
    login = normalLogin.TestLogin()
    login.test_tourist_login()
    home_search = TestSearch()
    home_search.test_search_home()
    login.teardown()

