
import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@pytest.fixture
def driver():
  driver = webdriver.Firefox()
  driver.maximize_window()
  yield driver
  driver.quit()

def test_sauce_demo_store(driver):
  url = "https://www.saucedemo.com/"
  driver.get(url)

 # 1. Авторизация
  login_page = LoginPage(driver, timeout=10)
  login_page.login("standard_user", "secret_sauce")

# 2. Страница товаров: ждём загрузки, добавляем товары
  inventory_page = InventoryPage(driver, timeout=10)
  inventory_page.wait_for_inventory_loaded()

  inventory_page.add_item("sauce-labs-backpack")
  inventory_page.wait_until_removed_button_appears("sauce-labs-backpack")

  inventory_page.add_item("sauce-labs-bolt-t-shirt")
  inventory_page.add_item("sauce-labs-onesie")

# Переход в корзину
  inventory_page.open_cart()

# 3. Страница корзины: переходим к оформлению
  cart_page = CartPage(driver, timeout=10)
  cart_page.proceed_to_checkout()

# 4. Оформление покупки
  checkout_page = CheckoutPage(driver, timeout=10)
  checkout_page.fill_personal_info("Вячеслав", "Безгин", "672000")
  checkout_page.continue_checkout()

# Проверка итоговой суммы
  total = checkout_page.get_total_amount()
  assert total == 58.29, f"Ожидалась сумма 58.29, но получена {total}"