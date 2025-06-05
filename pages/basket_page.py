from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_cart(self):
        assert self.is_element_present(*BasketPageLocators.CART_EMPTY_BLOCK), "Cart is not empty"

    def should_be_text_of_empty_cart(self):
        assert self.browser.find_element(*BasketPageLocators.CART_EMPTY_BLOCK).text != "", "There is no 'Your basket is empty' message in cart"