from selenium import webdriver
from selenium.webdriver.common.by import By

class ResultsForm:

    def __init__(self, driver):
        self.driver = driver

    def get_results(self):
        url = self.driver.current_url
        city_title = self.driver.find_element(By.XPATH, "//div[@id='forecast_list_ul']//tr[1]/td[2]//a[contains(""@href,'/city/')]").text
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

    def exp_results_01(self):
        expected_results = {
            "url": 'https://openweathermap.org/find?q=Ha+Noi',
            "city_title": 'Ha Noi, VN',
            "temperature": '31°С',
            "width_logo": '50',
            "height_logo": '50'}
        return expected_results

    """def compare_results(self, actual_results, expected_results):
        self.assertEqual(actual_results['url'], expected_results['url'])
        self.assertEqual(actual_results['city_title'], expected_results['city_title'])
        try:
            self.assertEqual(actual_results['temperature'], expected_results['temperature'])
        except AssertionError:
            print('temperature expect not matching with actual ')
        self.assertEqual(actual_results['width_logo'], expected_results['width_logo'])
        self.assertEqual(actual_results['height_logo'], expected_results['height_logo'])"""




