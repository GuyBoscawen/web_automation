import time

import driver_helpers

_NATE_START_PAGE = 'https://nate-eu-west-1-prediction-test-webpages.s3-eu-west-1.amazonaws.com/tech-challenge/page1.html'


def _fetch_nate_tech_challenge_start_page(driver, results):
    driver.get(_NATE_START_PAGE)
    driver.maximize_window()


def _navigate_page_1(driver, results):
    driver_helpers.click_element_by_tag_name(driver, "input")


def _navigate_page_2(driver, results, customer_info):
    time.sleep(13)
    city = customer_info['city'].capitalize()
    driver_helpers.click_element_by_class_name(driver, "custom-select-trigger")
    driver_helpers.click_element_by_xpath(driver, f'//span[text()="{city}"]')
    driver_helpers.click_element_by_id(driver, "next-page-btn")


def _navigate_page_3(driver, results, customer_info):
    time.sleep(5)
    driver.execute_script(f'document.getElementById("popup").hidden=true;')
    driver_helpers.fill_element_by_id(driver, 'name', customer_info['name'])
    driver_helpers.fill_element_by_id(driver, 'pwd', customer_info['password'])
    driver_helpers.fill_element_by_id(driver, 'phone', customer_info['phone'])
    driver_helpers.fill_element_by_id(driver, 'email', customer_info['email'])
    driver_helpers.click_element_by_id(driver, 'defaultCheck2')
    driver_helpers.click_element_by_id(driver, 'btn')


def get_actions(customer_info):
    return [
        lambda driver, results: _fetch_nate_tech_challenge_start_page(driver, results),
        lambda driver, results: _navigate_page_1(driver, results),
        lambda driver, results: _navigate_page_2(driver, results, customer_info),
        lambda driver, results: _navigate_page_3(driver, results, customer_info),
    ]
