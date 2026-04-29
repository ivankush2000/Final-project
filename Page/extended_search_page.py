import allure
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ExtendedSearchPage(BasePage):
    # ссылка для перехода в расширенный поиск (используем contains, а не точный генерируемый класс)
    ADVANCED_SEARCH_LINK = "//a[contains(@class, 'advancedSearch')]"
    # выпадающий список "Тип поиска"
    # если стабилен, иначе data-tid
    SEARCH_TYPE_SELECT = "//select[@class='text el_6 __genreSB__']"
    # поле ввода имени актёра
    ACTOR_INPUT = "//input[@class='text ui-autocomplete-input']"
    # кнопка "Искать" для поиска по актеру
    SUBMIT_BUTTON = "//input[@id='btn_search_6']"
    # кнопка "Искать" для поиска по жанру
    SUBMIT_BUTTON_GENRE = '//input[@class="el_18 submit nice_button"]'

    @allure.step("Открыть расширенный поиск")
    def open_filter(self):
        """Клик по ссылке 'Расширенный поиск'."""
        link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.ADVANCED_SEARCH_LINK))
        )
        link.click()

    @allure.step("Выбрать тип поиска: {type_value}")
    def select_search_type(self, type_value: str = 'actor'):
        """Выбирает значение в выпадающем списке (например, 'actor')."""
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//option[@value='{type_value}']"))
        )
        option.click()

    @allure.step("Ввести актёра '{actor_partial}' и выбрать подсказку")
    def enter_actor_and_select(self, actor_partial: str):
        """
        Вводит часть имени актёра в поле и кликает по подсказке,
        содержащей эту строку.
        """
        name_actor = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.ACTOR_INPUT))
        )
        name_actor.clear()
        name_actor.send_keys(actor_partial)
        suggestion = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//span[contains(text(), "{actor_partial}")]')
            )
        )
        suggestion.click()

    @allure.step("Нажать 'Искать' (поиск по актёру)")
    def submit_search_actor(self):
        """Клик по кнопке 'Искать' для поиска по актеру."""
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON))
        )
        btn.click()

    @allure.step("Нажать 'Искать' (поиск по жанру)")
    def submit_search_genre(self):
        """Клик по кнопке 'Искать' для поиска по жанру."""
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON_GENRE))
        )
        btn.click()

    @allure.step("Выбрать жанр '{genre}'")
    def genre_select(self, genre):
        genre_xpath = f'//select[@class="text el_6 __genreSB__"]//option[contains(text(), "{genre}")]'
        genre_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, genre_xpath)))
        genre_option.click()
