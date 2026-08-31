from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def proceed_to_checkout(self):
        checkout_locator = (By.ID, "checkout")
        checkout_button = self.wait.until(EC.element_to_be_clickable(checkout_locator))
        checkout_button.click()