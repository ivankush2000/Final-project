import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Page:
    # Поиск
    SEARCH_INPUT = "//input[@name='kp_query']"

    # Реклама
    CLOSE_AD_BUTTON = "//button[@data-tid='CloseButton']"

    # Результаты поиска
    CARD_FIRST_FILM = "//div[@class='element most_wanted']"

    # Элементы для поиска по фильтру
    SEARCH_STRING_FILTER = "//a[@class='styles_advancedSearch__gn_09']"
    DROP_DOWN_LIST = "//option[@value='actor']"
    SEARCH_BAR_FILTER = "//input[@class='text ui-autocomplete-input']"
    SEARCH_BUTTON = "//input[@id='btn_search_6']"
    SPAN = '//span[contains(text(), "Джонни Депп")]'

    # Элементы для перехода в другой раздел
    genre = "вестерн"
    MOVIE_TICKETS = '//a[@href="/lists/movies/movies-in-cinema/?utm_source=kinopoisk&utm_term=webbutton"]'
    ELEMENT = '//h1[@class="styles_title__9HPZ9"]'
    GANRE = f'//select[@class="text el_6 __genreSB__"]//option[contains(text(), "{genre}")]'
    BUTTON = '//input[@class="el_18 submit nice_button"]'

    # Элементы для запуска трейлера
    name_film = "Тор"
    FILM_CARD = f'//div[@class="element most_wanted"]//a[contains(text(), "{name_film}")]'
    TRAILER = '//div[@class="styles_previewInfo__rcdO6"]'

 
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def close_ad_if_present(self):
        try:
            ad = self.driver.find_element(By.XPATH, self.CLOSE_AD_BUTTON)
            if ad.is_displayed():
                ad.click()
                time.sleep(0.5)
        except:
            pass

    def search_string(self, name):
        self.close_ad_if_present()
        search_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_INPUT))
        )
        search_input.click()
        search_input.clear()
        search_input.send_keys(name)
        search_input.send_keys(Keys.RETURN)
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CARD_FIRST_FILM))
        )

    def get_first_film_card_text(self) -> str:
        """Возвращает текст названия первого фильма в выдаче."""
        title = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CARD_FIRST_FILM))
        )
        return title.text

    def open_filter(self):
        search = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_STRING_FILTER))
        )
        search.click()

    def search_by_creators(self):
        list_select = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.DROP_DOWN_LIST))
        )
        list_select.click()

    def actor_input(self, name):
        name_actor = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_BAR_FILTER))
        )
        name_actor.clear()
        name_actor.send_keys(name)
        name_1 = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.SPAN)
            )
        )
        name_1.click()

    def clik_search_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_BUTTON))
        )
        button.click()

    def open_movie_tickets_section(self):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.MOVIE_TICKETS))
        )
        button.click()

    def page_check(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.ELEMENT))
        )
        return element.text

    def search_by_genre(self):
        genre = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.GANRE))
        )
        genre.click()

    def click_search_button_genre(self):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON))
        )
        button.click()

    def open_movie_card(self):
        card = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.FILM_CARD))
        )
        card.click()

    def launch_trailer(self):
        trailer = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.TRAILER))
        )
        trailer.click()


