from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):

        self.page = page

        # Locators
        self.cart_icon = page.locator(".shopping_cart_link")

        self.cart_badge = page.locator(".shopping_cart_badge")

        self.cart_items = page.locator(".cart_item")

        self.remove_buttons = page.locator(
            "button[data-test^='remove']"
        )

        self.continue_shopping_button = page.locator(
            "#continue-shopping"
        )

        self.checkout_button = page.locator(
            "#checkout"
        )

    def open_cart(self):

        self.cart_icon.click()

    def add_first_product_to_cart(self):

        self.page.locator(
            "button[data-test^='add-to-cart']"
        ).first.click()

    def remove_first_product(self):

        self.remove_buttons.first.click()

    def get_cart_badge_count(self):

        if self.cart_badge.count() > 0:
            return int(self.cart_badge.text_content())

        return 0

    def get_cart_item_count(self):

        return self.cart_items.count()

    def click_continue_shopping(self):

        self.continue_shopping_button.click()

    def click_checkout(self):

        self.checkout_button.click()
    