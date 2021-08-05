from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchLocator:
    def __init__(self, driver):
        self.driver = driver

        self.INPUT_BUTTON = "(//input[@type='text'])[1]"
        self.SUBMIT = "(//form[@role='search'])[1]"

    def search(self, keyword):
        self.driver.find_element(By.XPATH, self.INPUT_BUTTON).send_keys(keyword)
        self.driver.find_element(By.XPATH, self.SUBMIT).submit()

