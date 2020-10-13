'''
Created on Oct 6, 2020

@author: mukund
'''
import unittest

from selenium import webdriver
import constantfile

class BaseClass (unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Safari()
        self.driver.get(constantfile.ConstantFile.testUrl)
        self.driver.implicitly_wait(100)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
