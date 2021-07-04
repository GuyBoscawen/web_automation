from selenium import webdriver


def get_webdriver(driver_name):
    if driver_name == "chrome":
        driver = webdriver.Chrome(executable_path='./chromedriver')
    elif driver_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Unsupported driver " + driver_name)

    driver.implicitly_wait(10)
    return driver
