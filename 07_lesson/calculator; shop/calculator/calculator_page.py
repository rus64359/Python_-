from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC



class CalculatorPage:

    def __init__(self, driver, timeout=60):

        self.driver = driver

        self.wait = WebDriverWait(driver, timeout)



        # Локаторы

        self._delay_input_locator = (By.CSS_SELECTOR, "#delay")

        self._screen_locator = (By.CLASS_NAME, "screen")



    def set_delay(self, seconds: int):

        """Вводит значение задержки (в секундах) в поле #delay."""

        element = self.driver.find_element(*self._delay_input_locator)

        element.clear()

        element.send_keys(str(seconds))



    def click_button(self, text: str):

        """Нажимает кнопку калькулятора по тексту внутри <span>."""

        # На странице кнопки — это span с текстом (7, +, 8, = и т.п.)

        locator = (By.XPATH, f"//span[text()='{text}']")

        button = self.driver.find_element(*locator)

        button.click()



    def get_result(self) -> str:

        """Ждёт и возвращает текст результата из поля .screen."""

        element = self.wait.until(

            EC.visibility_of_element_located(self._screen_locator)

        )

        return element.text

