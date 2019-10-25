from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import sys
import time

MAX_WAIT = 10

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
        
    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)       

    def get_item_input_box(self):
        return self.wait_for(lambda: self.browser.find_element_by_id('id_text'))

    def get_error_message(self):
        return self.wait_for(lambda: self.browser.find_element_by_css_selector('.has-error'))

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])    

    def wait_for_row_in_list_table(self, row_text):
        self.wait_for(lambda: self.check_for_row_in_list_table(row_text))
        
    def add_new_item(self, item_name):
        inputbox = self.get_item_input_box()
        inputbox.send_keys(item_name)
        inputbox.send_keys(Keys.ENTER)
        
        