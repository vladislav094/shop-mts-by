
import allure
import pytest
from framework.features.shop_mts.shop_mts_app import ShopMtsApp
from framework.features.shop_mts.data.data_iphone import DataIphoneModels

@pytest.mark.usefixtures("set_up_webdriver")
class TestModuleSearch:

    @allure.description('In that test we testing search-module and assert result of search')
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.parametrize('phone_model', [
        DataIphoneModels.iphone_13_pro_256gb_gold,
        DataIphoneModels.iphone_13_pro_max_128gb_silver
    ])
    def test_search_iphone_and_assert_results(self, phone_model):
        shop_mts = ShopMtsApp(self.driver)
        main_page = shop_mts.main_page
        shop_mts.go_to_url("")
        main_page.find_search_field_and_input_models_phone(phone_model)
        main_page.get_nav_links_text()
        main_page.assert_lists_with_result_search(phone_model)


    @allure.description("In that test we try make order on Main page in Special Offers tab")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.parametrize('tabs, product_id, color_id', [
        ("new product", 0, 0),
        ("new product", 1, 0),
        ("new product", 2, 0),
        ("hits", 3, 0),
        ("hits", 4, 0),
        ("hits", 5, 0)
    ])
    def test_make_order(self, tabs, product_id, color_id):
        shop_mts = ShopMtsApp(self.driver)
        main_page = shop_mts.main_page
        shop_mts.go_to_url("")
        main_page.find_product_on_special_offers(tabs, product_id)
        main_page.choose_color_product(color_id)
        main_page.add_to_card()


