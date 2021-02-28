import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWorkWeixin:
    def setup(self):
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(5)
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:1000'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 企业微信注册demo
    # def test_register(self):
    #     self.driver.get("https://work.weixin.qq.com/")
    #     self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
    #     self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()
    #     self.driver.find_element(By.XPATH, "//*[@id='corp_name']").send_keys("test")
    #     sleep(5)

    # 浏览器复用后的操作，将浏览器开个调试口子复用已有的浏览器
    def test_login_with_debugger(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 用户已登录界面
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        self.driver.find_element(By.XPATH, "//*[@id='menu_apps']").click()
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()
        self.driver.find_element(By.XPATH, "//*[@id='menu_manageTools']").click()
        self.driver.find_element(By.XPATH, "//*[@id='menu_profile']").click()

    # 使用cookie进行登录
    def test_login_with_cookies(self):
        # 存入cookie
        cookies = self.driver.get_cookies()
        with open("./temp.txt", "w", encoding="utf-8") as f:
            f.write(json.dumps(cookies))
            print(cookies)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 读取cookie
        with open("./temp.txt", "r", encoding="utf-8") as f:
            cookies = json.loads(f.read())
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(5)
