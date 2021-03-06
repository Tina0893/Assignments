from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeworkDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "HW"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        # caps["settings[waitForIdleTimeout]"] = 1
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_contacts(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 官方滑动查找方式：向下滑动两次，再向上查找，直到找到元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().text("添加成员").'
                                                               'instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 如果页面中有很多个地方包含text='必填'，那这里要用什么定位元素好点？
        self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys("a001")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys("12313140001")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
