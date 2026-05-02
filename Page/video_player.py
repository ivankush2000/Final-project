import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class VideoPlayer:
    """
    Плеер трейлера во iframe виджета Кинопоиска:
    ждём iframe по одному CSS-селектору,
    затем внутри — элемент ``video``.
    """

    PLAYER_IFRAME = (By.CSS_SELECTOR, "iframe[src*='widgets.kinopoisk']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    @allure.step("Проверить наличие видеоплеера внутри iframe Кинопоиска")
    def video_inside_player_iframe(self) -> bool:
        """
        Ждёт появления iframe с виджетом и загрузки ``video`` внутри него.

        Returns:
            True, если ``video`` найден в iframe; иначе False.
        """
        inner_wait = WebDriverWait(self.driver, 20)

        with allure.step("Ожидание появления iframe виджета"):
            try:
                self.wait.until(
                    EC.presence_of_element_located(self.PLAYER_IFRAME)
                )
            except TimeoutException:
                allure.attach(
                    "Не удалось дождаться iframe виджета Кинопоиска",
                    name="iframe_timeout_error",
                    attachment_type=allure.attachment_type.TEXT
                )
                return False

        with allure.step("Поиск iframe-элементов на странице"):
            frames = self.driver.find_elements(*self.PLAYER_IFRAME)
            if not frames:
                return False

        with allure.step("Переключение в iframe и ожидание тега <video>"):
            try:
                self.driver.switch_to.frame(frames[0])
                inner_wait.until(
                    EC.presence_of_element_located((By.TAG_NAME, "video"))
                )
                return True
            except TimeoutException:
                allure.attach(
                    "Видео не загрузилось внутри iframe",
                    name="video_timeout_error",
                    attachment_type=allure.attachment_type.TEXT
                )
                return False
            finally:
                self.driver.switch_to.default_content()
