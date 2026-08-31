from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self._username_locator = (By.ID, "user-name")
        self._password_locator = (By.ID, "password")
        self._login_button_locator = (By.ID, "login-button")

    def login(self, username: str, password: str):
        username_input = self.wait.until(EC.element_to_be_clickable(self._username_locator))
        password_input = self.driver.find_element(*self._password_locator)
        login_button = self.driver.find_element(*self._login_button_locator)

        username_input.clear()
        username_input.send_keys(username)

        password_input.clear()
        password_input.send_keys(password)

        login_button.click()