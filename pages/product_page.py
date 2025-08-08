from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_able_to_add_to_basket(self):
        self.should_see_the_add_to_basket_button()
        self.should_add_to_basket()
        self.should_be_the_right_item()
        self.should_be_the_right_price()

    def should_see_the_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"
    
    def should_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()
    
    def should_be_the_right_item(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
        assert product_name == message_product_name, \
            f"Product name in basket message does not match. Expected '{product_name}', got '{message_product_name}'"
    
    def should_be_the_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET).text
        assert product_price == basket_price, \
            f"Basket price does not match product price. Expected '{product_price}', got '{basket_price}'"