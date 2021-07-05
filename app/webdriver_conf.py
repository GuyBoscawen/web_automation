from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_webdriver(driver_name):
    if driver_name == "chrome":
        driver = webdriver.Chrome(executable_path='./mac_drivers/chromedriver')
    elif driver_name == "firefox":
        driver = webdriver.Firefox(executable_path='./mac_drivers/geckodriver')
    elif driver_name == 'chrome_remote':
        capabilities = {
            'browserName': "chrome",
        }
        driver = webdriver.Remote(
            command_executor="http://host.docker.internal:4444/wd/hub",
            desired_capabilities=capabilities
        )
    elif driver_name == 'firefox_remote':
        capabilities = {
            'browserName': "firefox",
        }
        driver = webdriver.Remote(
            command_executor="http://host.docker.internal:4445/wd/hub",
            desired_capabilities=capabilities
        )
    else:
        raise Exception("Unsupported driver " + driver_name)

    driver.implicitly_wait(10)
    return driver
