from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class NextLink_Form(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver

    def click_city(self):
        self.driver.find_element(By.XPATH,
                                 "//div[@id='forecast_list_ul']//tr[1]/td[2]//a[contains(@href,'/city/')]").click()

    def get_weather_details(self):
        url = self.driver.current_url
        city_title = self.driver.find_element(By.XPATH, "//span[@class='orange-text']/following-sibling::h2").text
        temperature = self.driver.find_element(By.XPATH, "//span[@class='heading']").text
        results_details = {
            "url": url,
            "city_title": city_title,
            "temperature": temperature
        }
        return results_details

    def expected_results_detail_02(self):

        expected_results_detail = {
            "url": 'https://openweathermap.org/city/1581130',
            "city_title": 'Hanoi, VN',
            "temperature": '34°C'}

        return expected_results_detail

    def compare_details(self, actual_results_details, expect_results_details):

        self.assertEqual(actual_results_details['url'], expect_results_details['url'])
        self.assertEqual(actual_results_details['city_title'], expect_results_details['city_title'])
        try:
            self.assertEqual(actual_results_details['temperature'], expect_results_details['temperature'])
        except AssertionError:
            print('Temperature not matching')

