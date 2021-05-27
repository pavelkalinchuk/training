# -*- coding: utf-8 -*-
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
        wd.find_element_by_link_text("Logout").click()
        wd.close()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
