from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self._first_name_locator = (By.ID, "first-name")
        self._last_name_locator = (By.ID, "last-name")
        self._postal_code_locator = (By.ID, "postal-code")
        self._continue_button_locator = (By.ID, "continue")
        self._total_locator = (By.CLASS_NAME, "summary-total")

    def fill_personal_info(self, first_name: str, last_name: str, postal_code: str):
        first_name_input = self.wait.until(EC.element_to_be_clickable(self._first_name_locator))
        last_name_input = self.wait.until(EC.element_to_be_clickable(self._last_name_locator))
        postal_code_input = self.wait.until(EC.element_to_be_clickable(self._postal_code_locator))

        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input.clear()
        last_name_input.send_keys(last_name)

        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)

    def continue_checkout(self):
        continue_button = self.wait.until(EC.element_to_be_clickable(self._continue_button_locator))
        continue_button.click()

    def get_total_amount(self) -> float:
        total_element = self.wait.until(EC.visibility_of_element_located(self._total_locator))
        text = total_element.text # например, "$58.29"
        clean_text = text.replace("$", "")
        return float(clean_text)