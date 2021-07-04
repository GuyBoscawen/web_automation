import enum

from functools import wraps


class SELECTOR_TYPE(enum.Enum):
    ID = 'id'
    TAG = 'tag'
    CLASS = 'class'


class ACTION_TYPE(enum.Enum):
    CLICK = 'click'
    FILL = 'fill'


def capture_page_prior_to_action(f):
    @wraps(f)
    def decorated(driver, selector_id, *args, **kwargs):
        file_location = f'./tmp/img_logs/{f.__name__}_{selector_id}.png'
        driver.save_screenshot(file_location)

        with open(f'./tmp/html_logs/{f.__name__}_{selector_id}.html', 'w') as html_file:
            html_file.write(driver.page_source)
            html_file.close()

        return f(driver, selector_id, *args, **kwargs)

    return decorated


def append_action(action_type, selector_type):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if action_type == ACTION_TYPE.CLICK:
                if selector_type == SELECTOR_TYPE.ID:
                    args[0].execute_script(
                        f'document.getElementById("{args[1]}").setAttribute("nate-action-type", "{action_type}");'
                    )
                elif selector_type == SELECTOR_TYPE.TAG:
                    args[0].execute_script(
                        f'document.getElementsByTagName("{args[1]}")[0].setAttribute("nate-action-type", "{action_type}");'
                    )
                elif selector_type == SELECTOR_TYPE.CLASS:
                    args[0].execute_script(
                        f'document.getElementsByClassName("{args[1]}")[0].setAttribute("nate-action-type", "{action_type}");'
                    )
                else:
                    raise ValueError(
                        f'selector_type, {selector_type}, not allowed for action_type {action_type}'
                    )

            elif action_type == ACTION_TYPE.FILL:
                if selector_type == SELECTOR_TYPE.ID:
                    args[0].execute_script(
                        f'document.getElementById("{args[1]}").setAttribute("nate-dict-key", "{args[2]}");'
                    )
                else:
                    raise ValueError(
                        f'selector_type, {selector_type}, not allowed for action_type {action_type}'
                    )
            else:
                raise ValueError(
                    f'Unknown action_type, {action_type}'
                )

            return f(*args, **kwargs)
        return decorated
    return wrapper


@capture_page_prior_to_action
@append_action(ACTION_TYPE.FILL, SELECTOR_TYPE.ID)
def fill_element_by_id(driver, element_id, value):
    driver.find_element_by_id(
        element_id
    ).send_keys(
        value
    )


@capture_page_prior_to_action
@append_action(ACTION_TYPE.CLICK, SELECTOR_TYPE.ID)
def click_element_by_id(driver, element_id):
    driver.find_element_by_id(
        element_id
    ).click()


@capture_page_prior_to_action
@append_action(ACTION_TYPE.CLICK, SELECTOR_TYPE.TAG)
def click_element_by_tag_name(driver, tag_name):
    driver.find_element_by_tag_name(
        tag_name
    ).click()


@capture_page_prior_to_action
@append_action(ACTION_TYPE.CLICK, SELECTOR_TYPE.CLASS)
def click_element_by_class_name(driver, class_name):
    driver.find_element_by_class_name(
        class_name
    ).click()
