from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.config import (
    BASE_URL,
    VALID_USERNAME,
    VALID_PASSWORD
)


def login_and_add_product(page: Page):

    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    cart_page = CartPage(page)

    cart_page.add_first_product_to_cart()

    cart_page.open_cart()

    cart_page.click_checkout()


# TC_CHECKOUT_001
def test_successful_checkout(page: Page):

    login_and_add_product(page)

    checkout_page = CheckoutPage(page)

    checkout_page.enter_checkout_information(
        "Richa",
        "Sharma",
        "2000"
    )

    checkout_page.click_continue()

    checkout_page.click_finish()

    expect(
        checkout_page.checkout_complete_message
    ).to_contain_text(
        "Thank you for your order"
    )


# TC_CHECKOUT_002
def test_checkout_empty_first_name(page: Page):

    login_and_add_product(page)

    checkout_page = CheckoutPage(page)

    checkout_page.enter_checkout_information(
        "",
        "Sharma",
        "2000"
    )

    checkout_page.click_continue()

    expect(
        checkout_page.error_message
    ).to_contain_text(
        "First Name is required"
    )


# TC_CHECKOUT_003
def test_checkout_empty_last_name(page: Page):

    login_and_add_product(page)

    checkout_page = CheckoutPage(page)

    checkout_page.enter_checkout_information(
        "Richa",
        "",
        "2000"
    )

    checkout_page.click_continue()

    expect(
        checkout_page.error_message
    ).to_contain_text(
        "Last Name is required"
    )


# TC_CHECKOUT_004
def test_checkout_empty_postal_code(page: Page):

    login_and_add_product(page)

    checkout_page = CheckoutPage(page)

    checkout_page.enter_checkout_information(
        "Richa",
        "Sharma",
        ""
    )

    checkout_page.click_continue()

    expect(
        checkout_page.error_message
    ).to_contain_text(
        "Postal Code is required"
    )


# TC_CHECKOUT_005
def test_cancel_checkout(page: Page):

    login_and_add_product(page)

    checkout_page = CheckoutPage(page)

    checkout_page.click_cancel()

    expect(page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )


# TC_CHECKOUT_006
def test_checkout_summary_information(page: Page):

    login_and_add_product(page)

    checkout_page = CheckoutPage(page)

    checkout_page.enter_checkout_information(
        "Richa",
        "Sharma",
        "2000"
    )

    checkout_page.click_continue()

    expect(
        checkout_page.checkout_summary
    ).to_be_visible()