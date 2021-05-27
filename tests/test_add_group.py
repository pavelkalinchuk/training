# -*- coding: utf-8 -*-
import time

from selenium import webdriver
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path='/Users/pavelkalincuk/git/help_soft/chromedriver')
        self.wd.implicitly_wait(30)

    def test_(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("test_group")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("test")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("test")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
        time.sleep(3)
        wd.find_element_by_link_text("Logout").click()
        wd.close()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
