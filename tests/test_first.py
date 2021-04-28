 -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webwd.common.keys import Keys
# from selenium.webwd.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import pytest


class Test(unittest.TestCase):
    def setUp(self):
        self.wd = webwd.Chrome(executable_path='/Users/pavelkalincuk/git/help_soft/chromedriver')
        self.wd.implicitly_wait(30)

    def test_(self):
        driver = self.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("Logout").click()
        wd.close()

#    def is_element_present(self, how, what):
#        try:
#            self.wd.find_element(by=how, value=what)
#        except NoSuchElementException as e:
#            return False
#        return True
#
#    def is_alert_present(self):
#        try:
#            self.wd.switch_to_alert()
#        except NoAlertPresentException as e:
#            return False
#        return True
#
#    def close_alert_and_get_its_text(self):
#        try:
#            alert = self.wd.switch_to_alert()
#            alert_text = alert.text
#            if self.accept_next_alert:
#                alert.accept()
#            else:
#                alert.dismiss()
#            return alert_text
#        finally:
#            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
