from framework.features.shop_mts.locators.main_page_locators import MainPageLocators
from framework.features.shop_mts.locators.product_page_locator import ProductPageLocators

from framework.utils import SeleniumBase


class PageElements:
    def __init__(self, driver):
        self.driver = driver
        self.locator_main_page = MainPageLocators
        self.product_page_locator = ProductPageLocators

    @property
    def selenium(self):
        return SeleniumBase(driver=self.driver)

    @property
    def search_field(self):
        return SeleniumBase(driver=self.driver, locator=self.locator_main_page.SEARCH_FIELD)

    @property
    def search_button(self):
        return SeleniumBase(driver=self.driver, locator=self.locator_main_page.SEARCH_BUTTON)

    @property
    def links_product(self):
        return SeleniumBase(driver=self.driver, locator=self.locator_main_page.LINKS_PRODUCT)

    @property
    def nav_bar(self):
        return SeleniumBase(driver=self.driver, locator=self.locator_main_page.NAV_BAR)

    @property
    def tab_hits(self):
        return SeleniumBase(driver=self.driver, locator=self.locator_main_page.TAB_HITS)

    @property
    def tab_new_product(self):
        return SeleniumBase(driver=self.driver, locator=self.locator_main_page.TAB_NEW_PRODUCT)

    @property
    def all_stocks(self):
        return SeleniumBase(driver=self.driver, locator=self.locator_main_page.ALL_STOCKS)

    @property
    def color(self):
        return SeleniumBase(driver=self.driver, locator=self.locator_main_page.COLOR)

    @property
    def add_to_cart_button(self):
        return SeleniumBase(driver=self.driver, locator=self.product_page_locator.ADD_TO_CARD_BUTTON)

