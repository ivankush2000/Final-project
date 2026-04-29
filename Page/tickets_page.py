import allure
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TicketsPage(BasePage):
    MOVIE_TICKETS_LINK = '//a[@href="/lists/movies/movies-in-cinema/?utm_source=kinopoisk&utm_term=webbutton"]'
    HEADER = '//h1[contains(@class, "styles_title")]'

    @allure.step("Перейти в раздел 'Билеты в кино'")
    def open_tickets_section(self):
        btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.MOVIE_TICKETS_LINK)))
        btn.click()

    @allure.step("Получить заголовок страницы")
    def get_page_header(self) -> str:
        header = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.HEADER)))
        return header.text.strip()