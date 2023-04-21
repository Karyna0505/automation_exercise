import allure
import random
import string


def take_screenshot(page, name) -> None:
    allure.attach(
        body=page.screenshot(full_page=True),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )


def generate_random_email():
    letters = string.ascii_lowercase
    email = ''.join(random.choice(letters) for i in range(10))
    email += '@example.com'
    return email
