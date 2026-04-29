import allure
import pytest
from Page.base_page import BasePage
from Page.search_results_page import SearchResultsPage
from Page.extended_search_page import ExtendedSearchPage
from Page.movie_page import MoviePage
from Page.tickets_page import TicketsPage


@allure.feature("Поиск по поисковой строке")
@allure.story("Поиск по названию фильма")
@pytest.mark.parametrize("query, expected", [
    ("Леон", "Леон"),
    ("Leon", "Леон"),
    ("Человек-паук", "Человек-паук"),
    ("Человек-паук 2", "Человек-паук 2"),
    ("Человек дождя", "Человек дождя"),
    ("Шазам!", "Шазам!"),
])
def test_search(driver, query, expected):
    with allure.step(f"Поиск '{query}', ожидается '{expected}'"):
        main = BasePage(driver)
        main.search(query)
        results = SearchResultsPage(driver)
        title = results.get_first_film_title()
        assert expected.lower() == title.lower(
        ), f"Ожидался '{expected}', получен '{title}'"


@allure.feature("Поиск по актеру")
@allure.story("Поиск по актёру")
def test_search_by_actor(driver):
    act = "Джонни Деп"
    with allure.step(f"Поиск фильмов с актёром {act}"):
        main = BasePage(driver)
        main.close_ad_if_present()
        extended = ExtendedSearchPage(driver)
        extended.open_filter()
        extended.select_search_type('actor')
        extended.enter_actor_and_select(act)
        extended.submit_search_actor()
        results = SearchResultsPage(driver)
        assert act in results.get_all_page()


@allure.feature("Навигация")
@allure.story("Переход в раздел 'Билеты в кино'")
def test_checking_transition_to_another_section(driver):
    with allure.step("Проверить заголовок раздела билетов"):
        tickets = TicketsPage(driver)
        tickets.open_tickets_section()
        header = tickets.get_page_header()
        assert header == "Билеты в кино"


@allure.feature("Поиск по жанру")
@allure.story("Поиск по жанру")
def test_search_by_genre(driver):
    genre = "вестерн"
    with allure.step(f"Поиск фильмов жанра '{genre}'"):
        main = BasePage(driver)
        main.close_ad_if_present()
        extended = ExtendedSearchPage(driver)
        extended.open_filter()
        extended.genre_select(genre)
        extended.submit_search_genre()
        results = SearchResultsPage(driver)
        assert genre in results.get_all_page()


@allure.feature("Просмотр контента")
@allure.story("Запуск трейлера")
def test_launch_trailer(driver):
    movie_name = "Тор"
    with allure.step(f"Открыть карточку фильма '{movie_name}' и запустить трейлер"):
        main = BasePage(driver)
        main.search(movie_name)
        movie = MoviePage(driver, movie_name)
        movie.open_card_by_name()
        movie.launch_trailer()
