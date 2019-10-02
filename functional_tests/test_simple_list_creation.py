from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        print(self.server_url)
    
        self.browser.get(self.server_url)
        
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('작업', header_text)
        
        self.add_new_item('공작깃털 사기')
        
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: 공작깃털 사기')

        self.add_new_item('공작깃털을 이용해서 그물만들기')
        
        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물만들기')
        self.check_for_row_in_list_table('1: 공작깃털 사기')
        
        self.browser.quit()
        self.exec_firefox()
        
        print(self.server_url)
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('공작깃털 사기', page_text);
        self.assertNotIn('그물만들기', page_text);
        
        self.add_new_item('우유 사기')
        
        print(self.browser.current_url)
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('공작깃털 사기', page_text);
        self.assertNotIn('그물만들기', page_text);
        self.assertIn('우유 사기', page_text);

 