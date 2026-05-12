import re

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

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


# TC_PRODUCT_001
def test_product_list_displayed(page: Page):

    login_to_application(page)

    inventory_page = InventoryPage(page)

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    assert inventory_page.get_product_count() > 0


# TC_PRODUCT_002
def test_product_details_displayed(page: Page):

    login_to_application(page)

    inventory_page = InventoryPage(page)

    product_names = inventory_page.get_product_names()

    product_prices = inventory_page.get_product_prices()

    assert len(product_names) > 0

    assert len(product_prices) > 0

    expect(
        inventory_page.inventory_item_descriptions.first
    ).to_be_visible()

    expect(
        inventory_page.inventory_images.first
    ).to_be_visible()


# TC_PRODUCT_003
def test_sort_products_by_name(page: Page):

    login_to_application(page)

    inventory_page = InventoryPage(page)

    inventory_page.sort_products("az")

    actual_names = inventory_page.get_product_names()

    expected_names = sorted(actual_names)

    assert actual_names == expected_names


# TC_PRODUCT_004
def test_sort_products_by_price(page: Page):

    login_to_application(page)

    inventory_page = InventoryPage(page)

    inventory_page.sort_products("lohi")

    actual_prices = inventory_page.get_product_prices()

    expected_prices = sorted(actual_prices)

    assert actual_prices == expected_prices


# TC_PRODUCT_005
def test_open_product_details_page(page: Page):

    login_to_application(page)

    inventory_page = InventoryPage(page)

    first_product_name = (
        inventory_page.get_product_names()[0]
    )

    inventory_page.open_first_product()

    expect(page).to_have_url(
        re.compile(r"inventory-item\.html")
    )

    expect(page.locator(".inventory_details_name")).to_have_text(
        first_product_name
    )

# TC_PRODUCT_006
def test_sort_dropdown_visible(page: Page):

    login_to_application(page)

    inventory_page = InventoryPage(page)

    expect(
        inventory_page.sort_dropdown
    ).to_be_visible()

# TC_PRODUCT_007
def test_all_product_images_visible(page: Page):

    login_to_application(page)

    inventory_page = InventoryPage(page)

    image_count = (
        inventory_page.inventory_images.count()
    )

    for index in range(image_count):

        expect(
            inventory_page.inventory_images.nth(index)
        ).to_be_visible()


# TC_PRODUCT_008
def test_product_count_consistent_after_sorting(page: Page):

    login_to_application(page)

    inventory_page = InventoryPage(page)

    initial_count = (
        inventory_page.get_product_count()
    )

    inventory_page.sort_products("lohi")

    sorted_count = (
        inventory_page.get_product_count()
    )

    assert initial_count == sorted_count


# TC_PRODUCT_009
def test_sort_products_price_high_to_low(page: Page):

    login_to_application(page)

    inventory_page = InventoryPage(page)

    inventory_page.sort_products("hilo")

    actual_prices = (
        inventory_page.get_product_prices()
    )

    expected_prices = sorted(
        actual_prices,
        reverse=True
    )

    assert actual_prices == expected_prices


# TC_PRODUCT_010
def test_sort_products_name_z_to_a(page: Page):

    login_to_application(page)

    inventory_page = InventoryPage(page)

    inventory_page.sort_products("za")

    actual_names = (
        inventory_page.get_product_names()
    )

    expected_names = sorted(
        actual_names,
        reverse=True
    )

    assert actual_names == expected_names