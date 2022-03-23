import time
from selenium.webdriver.common.by import By
url = "https://www.google.com/"
user_name = "corporatesales@poorvika.in"
password = "corporate@3456"


class Google:
    def __init__(self, driver):
        self.driver = driver

    def next_button(self):
        for next_username in self.driver.find_elements(By.CLASS_NAME, "VfPpkd-vQzf8d"):
            if next_username.text == "Next":
                print(next_username.text)
                next_username.click()
                break
        time.sleep(5)
        self.driver.implicitly_wait(3)

    def username(self):
        self.driver.find_element(By.TAG_NAME, "input").send_keys(user_name)
        Google.next_button(self)

    def user_pass(self):
        self.driver.find_element(By.CLASS_NAME,"whsOnd").send_keys(password)
        Google.next_button(self)

    def login(self):
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.CLASS_NAME,"gb_1").click()
        Google.username(self)
        Google.user_pass(self)





