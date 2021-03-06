from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWeworkAddress:
    # 基于浏览器复用账号登录
    def setup(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:1000'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)

    def test_login_with_debugger(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 用户已登录界面
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

        # 不可交互
        # 1. 元素被遮挡：元素前面还有其它不可见元素
        # 2. 元素有多个，需要人工挑选中合适的元素
        def wait_name(driver):
            driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[
                1].click()  # 元素不可交互，元素所在页面尚未加载完全
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_name)
        # 或者 self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[-1].click()

        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys('testName001')
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys('testAcct001')
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_mail']").send_keys('testAcct001@qq.com')
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()
