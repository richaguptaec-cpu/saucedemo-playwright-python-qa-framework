from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

from utils.config import (
    BASE_URL,
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    LOCKED_USERNAME
)


# TC_LOGIN_001
def test_successful_login(page: Page):

    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)

    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


# TC_LOGIN_002
def test_invalid_login(page: Page):

    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)

    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    expect(login_page.error_message).to_contain_text("Epic sadface")


# TC_LOGIN_003
def test_empty_username(page: Page):

    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)

    login_page.login("", VALID_PASSWORD)

    expect(login_page.error_message).to_contain_text("Username is required")


# TC_LOGIN_004
def test_empty_password(page: Page):

    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)

    login_page.login(VALID_USERNAME, "")

    expect(login_page.error_message).to_contain_text("Password is required")


# TC_LOGIN_005
def test_locked_user_login(page: Page):

    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)

    login_page.login(LOCKED_USERNAME, VALID_PASSWORD)

    expect(login_page.error_message).to_contain_text(
        "Sorry, this user has been locked out"
    )