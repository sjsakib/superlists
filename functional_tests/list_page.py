from selenium.webdriver.common.keys import Keys
from .base import wait


class ListPage(object):

    def __init__(self, test):
        self.test = test

    def get_item_input_box(self):
        return self.test.browser.find_element_by_id('id_text')

    def get_share_box(self):
        return self.test.browser.find_element_by_css_selector(
            'input[name="sharee"]'
        )

    def get_shared_with_list(self):
        return self.test.browser.find_elements_by_css_selector(
            '.list-sharee'
        )

    def get_list_owner(self):
        return self.test.browser.find_element_by_id('id_list_owner').text

    def share_list_with(self, email):
        self.get_share_box().send_keys(email)
        self.get_share_box().send_keys(Keys.ENTER)
        self.test.wait_for(lambda: self.test.assertIn(
            email,
            [item.text for item in self.get_shared_with_list()]
        ))

    def add_list_item(self, item_text):
        num_rows = len(self.test.browser.find_elements_by_css_selector('#id_list_table tr'))
        self.get_item_input_box().send_keys(item_text)
        self.get_item_input_box().send_keys(Keys.ENTER)
        item_number = num_rows + 1
        self.wait_for_row_in_list_table(f'{item_number}: {item_text}')
        return self

    @wait
    def wait_for_row_in_list_table(self, row_text):
        table = self.test.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.test.assertIn(row_text, [row.text for row in rows])
