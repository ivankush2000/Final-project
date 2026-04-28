import pytest
from Page.MainPage import Page


@pytest.mark.parametrize(
    "query, expected",
    [
        ("Леон", "Леон"),
        ("Leon", "Леон"),
        ("Человек-паук", "Человек-паук"),
        ("Человек-паук 2", "Человек-паук 2"),
        ("Человек дождя", "Человек дождя"),
        ("Шазам!", "Шазам!"),
    ],
)
def test_search(driver, query, expected):
    main = Page(driver)
    main.search_string(query)
    card_text = main.get_first_film_card_text()
    assert (
        expected.lower() in card_text.lower()
    ), f"Ожидалось '{expected}', но в карточке '{card_text}'"


def test_search_by_actor(driver):
    actor = "Джонни Деп"
    main = Page(driver)
    main.open_filter()
    main.search_by_creators()
    main.actor_input(actor)
    main.clik_search_button()


def test_checking_transition_to_another_section(driver):
    main = Page(driver)
    main.open_movie_tickets_section()
    name = main.page_check()
    assert name == "Билеты в кино"


def test_search_by_genre(driver):
    main = Page(driver)
    main.open_filter()
    main.search_by_genre()
    main.click_search_button_genre()


def test_launch_trailer(driver):
    film = "Тор"
    main = Page(driver)
    main.search_string(film)
    main.open_movie_card()
    main.launch_trailer()

