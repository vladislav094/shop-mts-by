from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class SeleniumBase:
    def __init__(self, driver, locator=None):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 20, 0.5)
        self.actions = webdriver.ActionChains(driver)
        self.locator = locator

    def find_if_visible(self) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located(self.locator))

    def find_if_present(self) -> WebElement:
        """Waiting on element and return WebElement if it is present on DOM"""
        return self.__wait.until(ec.presence_of_element_located(self.locator))

    def find_if_not_present(self) -> WebElement:
        """Wait on element until it disappears"""
        return self.__wait.until(ec.invisibility_of_element_located(self.locator))

    def find_if_are_visible(self) -> List[WebElement]:
        """Waiting on elements and return WebElements if they are visible"""
        return self.__wait.until(ec.visibility_of_all_elements_located(self.locator))

    def find_if_are_present(self) -> List[WebElement]:
        """Waiting on elements and return WebElements if they are present on DOM"""
        return self.__wait.until(ec.presence_of_all_elements_located(self.locator))

    @staticmethod
    def get_text_from_webelements(elements: List[WebElement]) -> List[str]:
        """The input should be a list of WebElements, where we read text from each element and Return a List[String]"""
        return [element.text for element in elements]

    @staticmethod
    def get_element_by_text(elements: List[WebElement], name: str) -> WebElement:
        """The input should we a list of WebElements, from which we return a single WebElement found by it's name"""
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def hover_cursor(self, element: WebElement) -> WebElement:
        """This method moves the mouse to the middle of the element.
        The element is also scrolled into the view on performing this action."""
        return self.actions.move_to_element(element).perform()

    def scroll(self, width: int, height: int):
        """The function scrolls the page to the specified height"""
        return self.driver.execute_script(f"window.scrollTo({width}, {height})")

    def new_tab(self) -> WebElement:
        """Opening a new tab in driver"""
        return self.driver.execute_script("window.open()")

    def view_handles(self) -> List[WebElement]:
        """Getting a list of all open tabs"""
        return self.driver.window_handles

    def switch_tab(self, number: int) -> WebElement:
        return self.driver.switch_to.window(number)

    def switch_frame(self, element: WebElement) -> WebElement:
        return self.driver.switch_to.frame(element)

    def click_elt(self, element: WebElement) -> WebElement:
        return self.__wait.until(ec.element_to_be_clickable(element)).click()

    def text_equal_to(self, value: str) -> WebElement:
        return self.__wait.until(ec.text_to_be_present_in_element((self.locator), value))

    def go_to_url(self, url: str) -> WebElement:
        return self.driver.get(url)

    def get_title_page(self) -> WebElement:
        return self.driver.title

    @staticmethod
    def input(web_element: WebElement, data: str):
        web_element.send_keys(data)

    def select_in_dropdown(self, value):
        Select(self.find_if_present()).select_by_visible_text(value)

    def scroll_to_elt(self, element: WebElement):
        return self.actions.scroll_to_element(element).perform()
