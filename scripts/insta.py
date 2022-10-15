from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import sys
from selenium.webdriver.common.by import By
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from functions import follow

class InstaBot:
    def __init__(self, username, password):
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
        user_agent_rotator = UserAgent(software_names=software_names,
                                       operating_systems= operating_systems,
                                       limit=100)
        user_agent = user_agent_rotator.get_random_user_agent()
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window_size=1420,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(f"--user-agent={user_agent}")
        
        PROXY = "http://20.111.54.16:8123"
        
        prox = Proxy()
        prox.proxy_type = ProxyType.MANUAL
        prox.autodetect = False
        capabilities = webdriver.DesiredCapabilities.CHROME
        prox.http_proxy = PROXY
        prox.ssl_proxy = PROXY 
        prox.acceptSslCerts = True
        prox.add_to_capabilities(capabilities)
        
        # self.driver = webdriver.Chrome(options = chrome_options, desired_capabilities = capabilities)
        # self.driver.get('http://lumtest.com/myip.json')
        self.driver = webdriver.Chrome(options = chrome_options)
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Autoriser')]")\
            .click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name=\"username\"]") \
            .send_keys(username)
        self.driver.find_element(By.XPATH,"//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element(By.XPATH,'//button[@type="submit"]') \
            .click()
        sleep(8)
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Plus tard')]")\
            .click()
        sleep(3)
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Plus tard')]")\
            .click()
        sleep(3)
        
    def bot_follow(self, key:str):
        follow(self, key)

if __name__ == "__main__":
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    if "-u" and "-p" in opts:
        print(args[0]+"@"+args[1])
        bot = InstaBot(args[0], args[1])
        if "-f" in opts:
            bot.bot_follow("#paris")
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")
