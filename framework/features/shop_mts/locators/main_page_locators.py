
from selenium.webdriver.common.by import By


class MainPageLocators:
	SEARCH_FIELD = (By.XPATH, '//*[@id="title-search-input"]')
	SEARCH_BUTTON = (By.XPATH, '//*[@id="title-search"]/button')
	LINKS_PRODUCT = (By.XPATH, '//a[@class="linkTovar"]')
	NAV_BAR = (By.XPATH, '//nav[@class="nav nav--header"]')
	TAB_HITS = (By.XPATH, '//span[text()="Хиты"]')
	TAB_NEW_PRODUCT = (By.XPATH, '//span[text()="Новинки"]')
	ALL_STOCKS = (By.XPATH, '/html/body/main/div[6]/div/div[1]/a')
	COLOR = (By.XPATH, '//label[@class="item__color__unit"]')
