from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

# Локаторы кнопок «Add to cart» и «Remove»
        self._inventory_item_locator = (By.CLASS_NAME, "inventory_item")

    def _get_add_button_locator(self, item_name: str) -> tuple:
# item_name — часть ID 
        return (By.ID, f"add-to-cart-{item_name}")

    def _get_remove_button_locator(self, item_name: str) -> tuple:
        return (By.ID, f"remove-{item_name}")

    def wait_for_inventory_loaded(self):
        """Ждёт появления хотя бы одного товара."""
        self.wait.until(EC.visibility_of_element_located(self._inventory_item_locator))

    def add_item(self, item_id_suffix: str):
        """Добавляет товар по суффиксу ID (например, 'sauce-labs-backpack')."""
        add_btn_locator = self._get_add_button_locator(item_id_suffix)
        add_button = self.wait.until(EC.element_to_be_clickable(add_btn_locator))
        add_button.click()

    def wait_until_removed_button_appears(self, item_id_suffix: str):
        """Ждёт, пока кнопка «Add» сменится на «Remove»."""
        remove_btn_locator = self._get_remove_button_locator(item_id_suffix)
        self.wait.until(EC.text_to_be_present_in_element(remove_btn_locator, "Remove"))

    def open_cart(self):
        cart_locator = (By.CLASS_NAME, "shopping_cart_container")
        cart_button = self.wait.until(EC.element_to_be_clickable(cart_locator))
        cart_button.click()