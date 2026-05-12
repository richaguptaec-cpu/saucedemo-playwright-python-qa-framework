from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):

        self.page = page

        # Locators
        self.inventory_items = page.locator(".inventory_item")

        self.inventory_item_names = page.locator(".inventory_item_name")

        self.inventory_item_prices = page.locator(".inventory_item_price")

        self.inventory_item_descriptions = page.locator(
            ".inventory_item_desc"
        )

        self.inventory_images = page.locator(".inventory_item_img img")

        self.sort_dropdown = page.locator(
            "[data-test='product-sort-container']"
        )

    def get_product_count(self):

        return self.inventory_items.count()

    def get_product_names(self):

        return self.inventory_item_names.all_text_contents()

    def get_product_prices(self):

        prices = self.inventory_item_prices.all_text_contents()

        return [
            float(price.replace("$", ""))
            for price in prices
        ]

    def sort_products(self, sort_option: str):

        self.sort_dropdown.select_option(sort_option)

    def open_first_product(self):

        self.inventory_item_names.first.click()

    