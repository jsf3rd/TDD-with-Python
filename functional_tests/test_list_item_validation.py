from .base import FunctionalTest
from unittest import skip
import time
from messages import EMPTY_LIST_ERROR, DUPLICATE_ITEM_ERROR

BUY_MILK = "우유사기"
MAKE_TEA = "tea 만들기"
BUY_COKE = "콜라 사기"

class ItemValidationTest(FunctionalTest):
        
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)

        self.add_new_item('')
        error = self.get_error_element()
        self.assertEqual(error.text, EMPTY_LIST_ERROR)
        
        self.add_new_item(BUY_MILK)
        self.wait_for_row_in_list_table('1: ' + BUY_MILK)
        
        self.add_new_item('')
        self.wait_for_row_in_list_table('1: ' + BUY_MILK)
        error = self.get_error_element()
        self.assertEqual(error.text, EMPTY_LIST_ERROR)
        
        self.add_new_item(MAKE_TEA)
        self.wait_for_row_in_list_table('1: ' + BUY_MILK)
        self.wait_for_row_in_list_table('2: ' + MAKE_TEA)
 
    def test_cannot_add_duplicate_items(self):
        self.browser.get(self.server_url)
        self.add_new_item(BUY_COKE)
        self.wait_for_row_in_list_table('1: ' + BUY_COKE)
        
        self.add_new_item(BUY_COKE)
        self.wait_for_row_in_list_table('1: ' + BUY_COKE)
        error = self.get_error_element()
        self.assertEqual(error.text, DUPLICATE_ITEM_ERROR)
        
        
    def test_error_messages_are_cleared_on_input(self):
        self.browser.get(self.server_url)
        self.add_new_item('')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())
        
        self.get_item_input_box().send_keys('a')
        
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
        