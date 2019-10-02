from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
        
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.add_new_item('')
        
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "빈 아이템을 등록할 수 없습니다")
        
        self.add_new_item('우유사기')
        self.check_for_row_in_list_table('1: 우유사기')
        
        self.add_new_item('')

        self.check_for_row_in_list_table('1: 우유사기')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "빈 아이템을 등록할 수 없습니다")
        
        self.add_new_item('tea 만들기')
        self.check_for_row_in_list_table('1: 우유사기')
        self.check_for_row_in_list_table('2: tea 만들기')
 