import pytest
import requests
import allure
import os
from dotenv import load_dotenv

load_dotenv()
url_api = os.getenv("base_url")
api_key = {"x-api-key": os.getenv("api_key")}


@pytest.mark.api
@allure.feature("Поиск фильмов")
@allure.story("Фильтрация по году и жанру")
@allure.severity(allure.severity_level.NORMAL)
def test_search_movie_by_year_and_genre():
    """Позитивный тест: поиск фильмов по году 2023 и жанру 'криминал'."""
    params = {"year": "2023", "genres.name": "криминал"}

    with allure.step(
        "Отправить GET-запрос на /v1.4/movie с нужными параметрами"
    ):
        response = requests.get(
            url=f"{url_api}v1.4/movie", params=params, headers=api_key
        )

    with allure.step("Проверить, что статус-код ответа равен 200"):
        assert response.status_code == 200

    with allure.step(
        "Проверить, что ответ содержит список фильмов в поле 'docs'"
    ):
        data = response.json()
        assert "docs" in data
        assert len(data["docs"]) > 0


@pytest.mark.api
@allure.feature("Поиск фильмов")
@allure.story("Фильтрация по рейтингу IMDb")
@allure.severity(allure.severity_level.NORMAL)
def test_search_movie_by_rating_range():
    """Позитивный тест: поиск фильмов с рейтингом IMDb от 8 до 10."""
    params = {"rating.imdb": "8-10"}

    with allure.step(
        "Отправить GET-запрос на /v1.4/movie с диапазоном рейтинга 8-10"
    ):
        response = requests.get(
            url=f"{url_api}v1.4/movie", params=params, headers=api_key
        )

    with allure.step("Убедиться, что сервер вернул 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что ответ содержит непустой массив docs"):
        data = response.json()
        assert "docs" in data
        assert (
            len(data["docs"]) > 0
        ), "Фильмы с рейтингом 8-10 должны существовать"


@pytest.mark.api
@allure.feature("Поиск фильмов")
@allure.story("Фильтрация по стране")
@allure.severity(allure.severity_level.NORMAL)
def test_search_movie_by_country():
    """Позитивный тест: поиск фильмов, снятых в России."""
    params = {"countries.name": "Россия"}

    with allure.step(
        "Отправить GET-запрос с параметром 'countries.name' = 'Россия'"
    ):
        response = requests.get(
            url=f"{url_api}v1.4/movie", params=params, headers=api_key
        )

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200

    with allure.step(
        "Убедиться, что в ответе есть фильмы (поле docs не пусто)"
    ):
        data = response.json()
        assert "docs" in data
        assert len(data["docs"]) > 0


@pytest.mark.api
@allure.feature("Получение фильма по ID")
@allure.story("Детальная информация о фильме")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movie_by_id():
    """Позитивный тест: получение информации о фильме по его ID."""
    movie_id = "301"
    url = f"{url_api}v1.4/movie/{movie_id}"

    with allure.step(f"Отправить GET-запрос на {url}"):
        response = requests.get(url, headers=api_key)

    with allure.step("Проверить, что статус-код ответа – 200"):
        assert response.status_code == 200

    with allure.step("Сравнить ID фильма в ответе с запрошенным"):
        data = response.json()
        assert "id" in data
        assert data["id"] == int(movie_id)
        allure.attach(
            str(data.get("name", "Нет названия")),
            name="Название фильма",
            attachment_type=allure.attachment_type.TEXT,
        )


@pytest.mark.api
@allure.feature("Поиск персон")
@allure.story("Поиск по имени")
@allure.severity(allure.severity_level.MINOR)
def test_search_person_by_name():
    """Позитивный тест: поиск персон по имени (Киану Ривз)."""
    params = {"name": "Киану Ривз"}

    with allure.step("Отправить GET-запрос на /v1.4/person с параметром name"):
        response = requests.get(
            url=f"{url_api}v1.4/person", params=params, headers=api_key
        )

    with allure.step("Проверить, что статус ответа равен 200"):
        assert response.status_code == 200

    with allure.step(
        "Проверить, что структура ответа – пагинированный о"
        "бъект с полем docs, и оно не пусто"
    ):
        data = response.json()
        assert "docs" in data, "Ответ должен содержать ключ 'docs'"
        assert isinstance(
            data["docs"], list
        ), "Значение 'docs' должно быть списком"
        assert len(data["docs"]) > 0, "Список персон не должен быть пустым"
        first_person = data["docs"][0]
        allure.attach(
            str(
                first_person.get(
                    "name", first_person.get("enName", "Без имени")
                )
            ),
            name="Первая персона в выдаче",
            attachment_type=allure.attachment_type.TEXT,
        )
