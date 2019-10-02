from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import sys
import time



class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            # print('arg: ' + arg)
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url
            
    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()
    
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