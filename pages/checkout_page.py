from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):

        self.page = page

        # Locators
        self.first_name_input = page.locator(
            "#first-name"
        )

        self.last_name_input = page.locator(
            "#last-name"
        )

        self.postal_code_input = page.locator(
            "#postal-code"
        )

        self.continue_button = page.locator(
            "#continue"
        )

        self.finish_button = page.locator(
            "#finish"
        )

        self.cancel_button = page.locator(
            "#cancel"
        )

        self.error_message = page.locator(
            "[data-test='error']"
        )

        self.checkout_summary = page.locator(
            ".summary_info"
        )

        self.checkout_complete_message = page.locator(
            ".complete-header"
        )

    def enter_checkout_information(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.first_name_input.fill(first_name)

        self.last_name_input.fill(last_name)

        self.postal_code_input.fill(postal_code)

    def click_continue(self):

        self.continue_button.click()

    def click_finish(self):

        self.finish_button.click()

    def click_cancel(self):

        self.cancel_button.click()
        