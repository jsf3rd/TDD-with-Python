from .base import FunctionalTest
from unittest import skip
import time
from messages import EMPTY_LIST_ERROR

BUY_MILK = "우유사기"
MAKE_TEA = "tea 만들기"

class ItemValidationTest(FunctionalTest):
        
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)

        self.add_new_item('')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, EMPTY_LIST_ERROR)
        
        self.add_new_item(BUY_MILK)
        self.check_for_row_in_list_table('1: ' + BUY_MILK)
        
        self.add_new_item('')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, EMPTY_LIST_ERROR)
        
        self.add_new_item(MAKE_TEA)
        self.check_for_row_in_list_table('1: ' + BUY_MILK)
        self.check_for_row_in_list_table('2: ' + MAKE_TEA)
 