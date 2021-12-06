from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


class InternetSpeedTwitterBot:
    def __init__(self, executable_path):
        # driver path
        self.chrome_driver_path = Service(executable_path)
        # driver object
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        # opening URL, of speed-testing website
        self.driver.get("https://fast.com/#")

        time.sleep(20)

        # this website automatically starts analyzing after loading,
        # after clicking on more info button we've no need
        # of clicking the start button again
        info_button = self.driver.find_element(By.ID, "show-more-details-link")
        info_button.click()

        time.sleep(60)

        # after waiting for operation to finish saving speed of down and up, extracting both speeds from web
        self.down = self.driver.find_element(By.ID, 'speed-value').text
        self.up = self.driver.find_element(By.ID, 'upload-value').text
        return f"{self.down}down/{self.up}up"

    def tweet_at_provider(self, username, password, message):

        # opening twitter login page
        self.driver.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5n"
                        "IjoicnUifQ%3D%3D%22%7D")

        # catching username and password elements and putting I.D and pass in it
        time.sleep(6)
        user_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                                        '/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]'
                                                        '/div/input')
        user_input.send_keys(username)
        user_input.send_keys(Keys.ENTER)

        time.sleep(2)
        pass_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                                        '/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/'
                                                        'div[2]/div/input')
        pass_input.send_keys(password)
        pass_input.send_keys(Keys.ENTER)

        # now logged inn, asking it to compose tweet
        time.sleep(3)
        compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/'
                                                     'div[1]/div[3]/a')
        compose.click()

        # writing a message in it
        time.sleep(3)
        message_box = self.driver.find_element(By.CLASS_NAME, 'public-DraftEditor-content')
        message_box.send_keys(message)

        # tweeting it
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                          '/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/'
                                                          'div/div[2]/div[3]/div/div/div[2]/div[4]/div')
        tweet_button.click()
