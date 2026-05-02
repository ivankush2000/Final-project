import allure
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MoviePage(BasePage):
    TRAILER = '//div[@class="styles_previewInfo__rcdO6"]'
    TRAILER_START_BUTTON = '//div[@class="styles_previewInfo__rcdO6"]'
    PLAY_BUTTON = '//button/label[text()="Остановить"]'

    def __init__(self, driver, movie_name: str):
        super().__init__(driver)
        self.movie_name = movie_name

    @allure.step("Открыть карточку фильма")
    def open_card_by_name(self):
        """Открывает карточку фильма по названию и ждёт загрузки страницы."""
        card_xpath = (
            f'//div[@class="element most_wanted"]//a[contains(text(), '
            f'"{self.movie_name}")]'
            )
        card = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, card_xpath)))
        card.click()
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.TRAILER)))

    @allure.step("Запустить трейлер")
    def launch_trailer(self):
        """Кликает по кнопке трейлера на странице фильма."""
        trailer_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.TRAILER_START_BUTTON)
        ))
        trailer_btn.click()
