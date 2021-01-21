import os
import subprocess
import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from suite.library.testData.testData import DataGenerator


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome: ")
# End Of Definition


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    # End of If Statement
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Execution is Finished")
# End Of Definition


@pytest.fixture(autouse=True)
def api_setup(request):
    path = os.path.abspath(find_path(os.path.dirname(os.path.realpath(__file__)))) + "\\basicApi.py"
    print(path)
    # os.system('START /B' + ' python ' + path)
    sp = subprocess.Popen(['python', path])
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", sp.pid)
    if not is_alive():
        print("API IS NOT WORKING")
        os.kill(sp.pid, 9)
    # End Of If Statement
    yield
    os.kill(sp.pid, 9)
# End Of Definition


def find_path(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == 'basicApi.py':
                return root
            # End Of If Statement
        # End Of For Loop
    # End Of For Loop


def is_alive():
    data_gen = DataGenerator()
    try:
        check_request = requests.get(data_gen.get_api())
        check_request.raise_for_status()
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return False
    except requests.exceptions.HTTPError:
        return False
    else:
        return True
    # End Of Try Statement
# End Of Definition
