from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

class NewVisitorTest(LiveServerTestCase):
    
    def exec_firefox(self):
        binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
        self.browser = webdriver.Firefox(firefox_binary=binary)
        self.browser.implicitly_wait(1)
        
    
    def setUp(self):
        self.exec_firefox()
        
    def tearDown(self):
        self.browser.quit()
        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def add_new_item(self, item_name):
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(item_name)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    def test_can_start_a_list_and_retrieve_it_later(self):
        print(self.live_server_url)
    
        self.browser.get(self.live_server_url)
        
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
        
        print(self.live_server_url)
        self.browser.get(self.live_server_url)
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
        
