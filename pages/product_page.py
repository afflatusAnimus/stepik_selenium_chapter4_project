from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        link.click()

    def should_be_correct_cart_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        cart_price_alert = self.browser.find_element(*ProductPageLocators.CART_PRICE_ALERT).text
        assert book_price == cart_price_alert, f"Diff between cart price '{cart_price_alert}' and price of added product '{book_price}'"

    def should_be_correct_product_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_added_to_cart_name =  self.browser.find_element(*ProductPageLocators.BOOK_ADDED_TO_CART_NAME).text
        assert book_name == book_added_to_cart_name, f"Diff between book name '{book_name}' and book added to cart name '{book_added_to_cart_name}'"