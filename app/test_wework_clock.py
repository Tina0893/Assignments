import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestClock:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "HW"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_clock(self):
        '''
        前提条件：已登录
        打卡用例：
        1、打开【企业微信】应用
        2、进入【工作台】
        3、点击【打卡】
        4、选择【外出打卡】tab
        5、点击【第N次打卡】
        6、验证【外出打卡成功】
        7、退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup//*[@text='工作台']").click()

        # 官方滑动查找方式：向下滑动两次，再向上查找，直到找到元素
        # android_uiautomator 里面要用双引号，外面用单引号
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()

        # 首次使用打卡功能时会有“立即使用”的弹窗，需要处理，否则找不到后续的打卡/外出打卡功能
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        print(self.driver.page_source)  # 打印当前页面结构

        # 方式一：加直接等待或显式等待
        time.sleep(2)
        assert "外出打卡成功" in self.driver.page_source  # 此处不是对元素的查找，隐式等待不生效

        # 方式二：激活setup中的隐式等待
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
