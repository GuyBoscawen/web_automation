import argparse
import time

import webdriver_conf
import website_actions

from website_actions import nate


def _execute_webdriver_actions(driver, results, actions):
    for action in actions:
        action(driver, results)
    time.sleep(5)


def _navigate_site(drivers):
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
        results = []

        _execute_webdriver_actions(driver, results, actions)

        driver.close()

        for result in results:
            print(args, result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web automation arguments")

    parser.add_argument(
        '-d', '--drivers',
        help='sets drivers in use',
        nargs='+',
        default=['firefox', 'chrome'],
        choices=['firefox', 'chrome']
    )

    args = parser.parse_args()
    _navigate_site(args.drivers)
