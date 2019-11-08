
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
HEADERS = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

class ChromeDrive:

    def __init__(self, driver_path="chromedriver"):
        print("工程路径：",os.getcwd())
        self.driver_path = driver_path
        self.header = HEADERS
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-gpu')
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=self.driver_path, options=chrome_options)


    def CloseOtherWindow(self, main_window):

        handles = self.driver.window_handles
        for h in handles:
            if h != main_window:
                self.driver.switch_to.window(h)
                print("切换窗口", self.driver.title)
                self.driver.close()
        self.driver.switch_to.window(main_window)