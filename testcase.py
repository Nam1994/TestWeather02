from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time


class VerifySearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://openweathermap.org/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def search(self, keyword):
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys(keyword)
        self.driver.find_element(By.XPATH, "(//form[@role='search'])[1]").submit()

    def get_results(self):
        url = self.driver.current_url
        city_title = self.driver.find_element(By.XPATH,
                                              "//div[@id='forecast_list_ul']//tr[1]/td[2]//a[contains(""@href,'/city/')]").text
        temperature = self.driver.find_element(By.XPATH, "(//span[@class='badge badge-info'])[1]").text
        logo = self.driver.find_element(By.XPATH, "(//td/img)[1]")
        width_logo = logo.get_attribute('width')
        height_logo = logo.get_attribute('height')
        results = {
            "url": url,
            "city_title": city_title,
            "temperature": temperature,
            "width_logo": width_logo,
            "height_logo": height_logo
        }
        return results

    def compare_results(self, actual_results, expected_results):
        self.assertEqual(actual_results['url'], expected_results['url'])
        self.assertEqual(actual_results['city_title'], expected_results['city_title'])
        try:
            self.assertEqual(actual_results['temperature'], expected_results['temperature'])
        except AssertionError:
            print('temperature expect not matching with actual ')
        self.assertEqual(actual_results['width_logo'], expected_results['width_logo'])
        self.assertEqual(actual_results['height_logo'], expected_results['height_logo'])

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

    def compare_details(self, actual_results_details, expect_results_details):
        self.assertEqual(actual_results_details['url'], expect_results_details['url'])
        self.assertEqual(actual_results_details['city_title'], expect_results_details['city_title'])
        try:
            self.assertEqual(actual_results_details['temperature'], expect_results_details['temperature'])
        except AssertionError:
            print('Temperature not matching')

    def test_search(self):
        # --> Enter text 'Ha Noi, VN' and submit input
        self.search('Ha Noi')
        # --> Form : Test url, title, temperature and logo
        expected_results = {
            "url": 'https://openweathermap.org/find?q=Ha+Noi',
            "city_title": 'Ha Noi, VN',
            "temperature": '31°С',
            "width_logo": '50',
            "height_logo": '50'
        }
        self.compare_results(self.get_results(), expected_results)
        # --> Click on link 'Ha Noi, VN'
        self.click_city()
        # --> test Temperature, text 'Ha Noi, VN', title
        expected_results_detail = {
            "url": 'https://openweathermap.org/city/1581130',
            "city_title": 'Hanoi, VN',
            "temperature": '34°C'
        }
        self.compare_details(self.get_weather_details(), expected_results_detail)


if __name__ == '__main__':
    unittest.main()
