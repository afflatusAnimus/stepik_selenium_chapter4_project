from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        link.click()

    def should_be_correct_cart_price(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == self.browser.find_element(*ProductPageLocators.CART_PRICE_ALERT).text, "Diff betwenn cart price and price of added product"

    def should_be_correct_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == self.browser.find_element(*ProductPageLocators.BOOK_ADDED_TO_CART_NAME).text, "Diff between book name and book added to cart name"