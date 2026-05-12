from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.cart_page import CartPage

from utils.config import (
    BASE_URL,
    VALID_USERNAME,
    VALID_PASSWORD
)


def login_to_application(page: Page):

    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )


# TC_CART_001
def test_add_product_to_cart(page: Page):

    login_to_application(page)

    cart_page = CartPage(page)

    cart_page.add_first_product_to_cart()

    expect(
        cart_page.cart_badge
    ).to_have_text("1")


# TC_CART_002
def test_remove_product_from_cart(page: Page):

    login_to_application(page)

    cart_page = CartPage(page)

    cart_page.add_first_product_to_cart()

    cart_page.open_cart()

    cart_page.remove_first_product()

    assert (
        cart_page.get_cart_item_count()
        == 0
    )


# TC_CART_003
def test_cart_badge_count(page: Page):

    login_to_application(page)

    cart_page = CartPage(page)

    cart_page.add_first_product_to_cart()

    assert (
        cart_page.get_cart_badge_count()
        == 1
    )


# TC_CART_004
def test_cart_page_displays_correct_products(page: Page):

    login_to_application(page)

    cart_page = CartPage(page)

    cart_page.add_first_product_to_cart()

    cart_page.open_cart()

    assert (
        cart_page.get_cart_item_count()
        > 0
    )


# TC_CART_005
def test_continue_shopping(page: Page):

    login_to_application(page)

    cart_page = CartPage(page)

    cart_page.add_first_product_to_cart()

    cart_page.open_cart()

    cart_page.click_continue_shopping()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )