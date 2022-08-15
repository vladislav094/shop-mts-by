
import pytest
from selenium import webdriver
from framework.common.env_vars import should_run_headless
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options as firefox_options




def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.100.7")
    parser.addoption("--bversion", action="store", default="103.0")
    parser.addoption("--width", action="store", default=1920)
    parser.addoption("--height", action="store", default=1080)

# @pytest.fixture
# def _get_chrome_options() -> webdriver.ChromeOptions:
#
#         """
#         Creates a set of options for running the Chrome browser.
#         Runs Chrome in headless mode depending on the value of the RUN_HEADLESS environment variable.
#         :return: A set of options to run the Chrome browser with.
#         """
#
#         chrome_options = webdriver.ChromeOptions()
#         run_headless = should_run_headless()
#
#         if run_headless:
#             chrome_options.add_argument("--headless")
#             chrome_options.add_argument("--disable-extensions")
#             chrome_options.add_argument("--disable-gpu")
#             chrome_options.add_argument("--no-sandbox")
#             chrome_options.add_argument("--disable-dev-shm-usage")
#             chrome_options.add_argument("--disable-setuid-sandbox")
#             chrome_options.add_argument("--ignore-ssl-errors=yes")
#             chrome_options.add_argument("--ignore-certificate-errors")
#
#         return chrome_options


@pytest.fixture
def get_webdriver(request):
    options = Options()
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    width = request.config.getoption("--width")
    height = request.config.getoption("--height")
    # executor_url = f"http://{executor}:4444/wd/hub"
    executor_url = f"https://selenium2-1.dev-bitrix.by/wd/hub/"
    # executor_url = f"https://192.168.100.20:4444/wd/hub/"

    if executor != 'local':
        capabilities = {
            "browserName" : browser,
            "browserVersion" : version,
            "screenResolution" : "1920x1080x24",
            "selenoid:options": {
                "enableVNC" : False
            }
        }


        driver = webdriver.Remote(
            desired_capabilities=capabilities,
            command_executor=executor_url,
            options=options
        )
    else:
        driver = webdriver.Chrome(options=options)

    driver.set_window_size(width, height)
    driver.implicitly_wait(30)
    return driver

@pytest.fixture
def get_actions(get_webdriver):
    actions = webdriver.ActionChains(get_webdriver)
    return actions

@pytest.fixture
def set_up_webdriver(request, get_webdriver, get_actions):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

