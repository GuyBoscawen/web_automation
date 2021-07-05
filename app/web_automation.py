import argparse
import time

import webdriver_conf

from website_actions import nate


def _execute_webdriver_actions(driver, actions):
    for action in actions:
        action(driver)
    time.sleep(5)


def _navigate_site(drivers):
    print('Navigating site')

    customer_info = {
        "city": "london",
        "name": "nate",
        "password": "07000000000",
        "email": "nate@nate.tech",
        "phone": "07000000000",
        "gender": "female"
    }

    actions = nate.get_actions(customer_info)

    for driver_name in drivers:
        driver = webdriver_conf.get_webdriver(driver_name)

        print(f'Starting execution with driver: {driver}')
        _execute_webdriver_actions(driver, actions)

        driver.close()

    print('success')
    return "success"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web automation arguments")

    parser.add_argument(
        '-d', '--drivers',
        help='sets drivers in use',
        nargs='+',
        default=['firefox', 'chrome'],
        choices=['firefox', 'chrome', 'firefox_remote', 'chrome_remote']
    )

    args = parser.parse_args()
    time.sleep(5)
    _navigate_site(args.drivers)
