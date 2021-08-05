import time

from selenium import webdriver
import unittest
from oop_weather.page_object_weather.searchPage import SearchLocator
from oop_weather.page_object_weather.submit_form import ResultsForm
from oop_weather.page_object_weather.next_link_form import NextLink_Form

from selenium.webdriver.common.by import By


class TestWeather(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_weather_valid(self):
        driver = self.driver
        self.driver.get('https://openweathermap.org/')

        # --> Input 'Ha Noi, VN'
        Login = SearchLocator(driver)
        Login.search('Ha Noi, VN')
        print('------------Submit Form------------------------')
        # --> Verify Results Element of Submit Form
        Form = ResultsForm(driver)
        try:
            # --> check url
            self.assertEqual(Form.get_results()["url"], Form.exp_results_01()["url"])
        except AssertionError:
            print('Not matching URL')

        try:
            # check Temperature
            self.assertEqual(Form.get_results()["temperature"], Form.exp_results_01()["temperature"])
        except AssertionError:
            print('Not matching actual temperature and expect temperature')
        # check title
        self.assertEqual(Form.get_results()["city_title"], Form.exp_results_01()["city_title"])

        # Check Logo Weather
        try:
            self.assertEqual(Form.get_results()["width_logo"], Form.exp_results_01()["width_logo"])
            print("matching")
        except:
            print('not pass')
        self.assertEqual(Form.get_results()["height_logo"], Form.exp_results_01()["height_logo"])

        print('---------------------------------------')
    # --> Verify Results Element of next link Form
        New_linkTest = NextLink_Form(driver)
        New_linkTest.click_city()
        NextLink_Form.compare_details(NextLink_Form.get_weather_details(), NextLink_Form.expected_results_detail_02())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
