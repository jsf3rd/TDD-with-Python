from .base import FunctionalTest


BUY_MILK = '우유사기'
BUY_FEATHERS = '공작깃털 사기'
MAKE_NET_WITH_FEATHER = '공작깃털을 이용해서 그물만들기'


class NewVisitorTest(FunctionalTest):
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        print(self.server_url)
    
        self.browser.get(self.server_url)
        
        header_text = self.wait_for(lambda: self.browser.find_element_by_tag_name('h1').text)
        self.assertIn('작업', header_text)
        
        self.add_new_item(BUY_FEATHERS)
        self.wait_for_row_in_list_table('1: ' + BUY_FEATHERS)
        
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        

        self.add_new_item(MAKE_NET_WITH_FEATHER)
        self.wait_for_row_in_list_table('1: ' + BUY_FEATHERS)
        self.wait_for_row_in_list_table('2: ' + MAKE_NET_WITH_FEATHER)
        
        self.browser.quit()
        self.exec_firefox()
        
        print(self.server_url)
        self.browser.get(self.server_url)
        page_text = self.wait_for(lambda: self.browser.find_element_by_tag_name('body').text)
        self.assertNotIn(BUY_FEATHERS, page_text);
        self.assertNotIn(MAKE_NET_WITH_FEATHER, page_text);
        
        self.add_new_item(BUY_MILK)
        self.wait_for_row_in_list_table('1: ' + BUY_MILK)        
        
        print(self.browser.current_url)
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        
        page_text = self.wait_for(lambda: self.browser.find_element_by_tag_name('body').text)
        self.assertNotIn(BUY_FEATHERS, page_text);
        self.assertNotIn(MAKE_NET_WITH_FEATHER, page_text);
        self.assertIn(BUY_MILK, page_text);

 