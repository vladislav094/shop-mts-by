import time

from framework.features.shop_mts.property_locators.all_page_property import PageElements
from framework.features.shop_mts.data.data_iphone import DataIphoneModels

class MainPage:
    def __init__(self, driver):
        self.element = PageElements(driver=driver)


    def find_search_field_and_input_models_phone(self, phone_model):
        search_field = self.element.search_field.find_if_visible()
        self.element.selenium.input(search_field, phone_model)
        search_button = self.element.search_button.find_if_visible()
        self.element.selenium.click_elt(search_button)


    def get_nav_links_text(self):
        return self.element.selenium.get_text_from_webelements(self.element.links_product.find_if_are_visible())


    def get_product_links(self):
        return self.element.links_product.find_if_are_present()


    def assert_lists_with_result_search(self, phone_model):
        list_iphone_models_gold = [DataIphoneModels.iphone_13_pro_256gb_gold, DataIphoneModels.iphone_13_pro_max_256gb_gold]
        if phone_model == DataIphoneModels.iphone_13_pro_256gb_gold:
            assert list_iphone_models_gold == self.get_nav_links_text()
        if phone_model == DataIphoneModels.iphone_13_pro_max_128gb_silver:
            assert DataIphoneModels.iphone_13_pro_max_128gb_silver == self.get_nav_links_text()[0]


    def find_product_on_special_offers(self, tabs: str, product_id: int):
        self.element.selenium.scroll_to_elt(self.element.all_stocks.find_if_present())
        if tabs == 'hits':
            self.element.selenium.click_elt(self.element.tab_hits.find_if_visible())
        else:
            self.element.selenium.click_elt(self.element.tab_new_product.find_if_visible())
        product = self.get_product_links()[product_id]
        self.element.selenium.click_elt(product)

    def choose_color_product(self, color_id: int):
        self.element.selenium.click_elt(self.element.color.find_if_are_visible()[color_id])
        time.sleep(2)

    def add_to_card(self):
        self.element.selenium.click_elt(self.element.add_to_cart_button.find_if_visible())


