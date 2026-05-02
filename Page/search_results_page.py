import allure
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SearchResultsPage(BasePage):
    CARD_FIRST_FILM = (
        "//div[@class='element most_wanted']//p[contains(@class, 'name')]/a"
        )

    @allure.step("Получить название первого фильма")
    def get_first_film_title(self) -> str:
        """Возвращает текст названия первого фильма из выдачи."""
        title_elem = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CARD_FIRST_FILM))
        )
        return title_elem.text.strip()

    @allure.step("Получить HTML всей страницы результатов")
    def get_all_page(self):
        return self.driver.page_source
