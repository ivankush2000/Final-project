import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    SEARCH_INPUT = "//input[@name='kp_query']"
    CLOSE_AD_BUTTON = "//button[@data-tid='CloseButton']"

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Закрыть рекламный баннер, если есть")
    def close_ad_if_present(self):
        """Закрывает рекламный баннер, если он есть и кликабелен."""
        try:
            ad = (WebDriverWait(self.driver, 2,
                                ignored_exceptions=[NoSuchElementException])
                  .until(EC.element_to_be_clickable((By.XPATH, self.CLOSE_AD_BUTTON))))
            ad.click()
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, self.CLOSE_AD_BUTTON))
            )
        except TimeoutException:
            pass

    @allure.step("Выполнить поиск по '{query}'")
    def search(self, query: str) -> None:
        """Вводит запрос в поисковую строку и нажимает Enter."""
        self.close_ad_if_present()
        search_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_INPUT))
        )
        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)
