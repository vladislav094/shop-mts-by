
from framework.features.shop_mts.pages.main_page import MainPage




class ShopMtsApp:
	def __init__(self, driver):
		self.driver = driver
		self.main_page = MainPage(self.driver)
		# self.sign_in_page = SignInPage(self.driver)
		self.url = "https://shop.mts.by/"

	def go_to_url(self, resource):
		self.driver.get(self.url + resource)


