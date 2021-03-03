from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.homePage.login_page import LoginPage


class HomePage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")

    def gotoLogin(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
        # 将类初始化成对象
        return LoginPage(self.driver)

    def gotoRegister(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_head_info_pCDownloadBtn']").click()

    def gotoDownload(self):
        pass
