from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def follow(self, key:str):
    self.driver.find_element(By.XPATH,"//input[@placeholder='Rechercher']") \
        .send_keys(key)
    sleep(4)
    self.driver.find_element(By.XPATH,"//input[@placeholder='Rechercher']") \
        .send_keys(Keys.DOWN)
    sleep(4)
    self.driver.find_element(By.XPATH,"//input[@placeholder='Rechercher']") \
        .send_keys(Keys.ENTER)
    # self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.DOWN)
    # sleep(1)
    # self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ENTER)
