import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from django.contrib.auth import get_user_model
User = get_user_model()


class MySeleniumTests(StaticLiveServerTestCase):
    # fixtures = ['user-data.json']

    def setUp(self):
        # 创建一个测试用户
        # 注意： user必须设置is_staff为True，不然登录不了admin后台
        User.objects.create_user(
            username='test', password='test', is_staff=True)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        """admin登录测试"""
        # 登录管理页面
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        # 填写用户名
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('test')
        # 填写密码
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test')
        # 点击「登录」按钮
        self.selenium.find_element_by_xpath(
            '//*[@id="login-form"]/div[3]/input').click()

        # 是否有注销url
        logout_link = self.selenium.find_element_by_link_text('注销')
        self.assertIsNotNone(logout_link)

        # # 弹出错误信息
        # errornote = self.selenium.find_element_by_class_name('errornote')
        # self.assertIsNone(errornote)

        # # 进入admin主页
        # site_name = self.selenium.find_element_by_xpath('//*[@id="site-name"]')
        # # self.assertIsNone(site_name)
        # self.assertIsNotNone(site_name)
        # # time.sleep(3)

    def test_error_password_login(self):
        """admin错误密码登录测试"""
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('test')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('error-password')
        self.selenium.find_element_by_xpath(
            '//*[@id="login-form"]/div[3]/input').click()

        # 弹出错误信息
        errornote = self.selenium.find_element_by_class_name('errornote')
        self.assertIsNotNone(errornote)

        # 登录页面也有 site-name
        # site_name = self.selenium.find_element_by_xpath('//*[@id="site-name"]')
        # self.assertIsNone(site_name)
        # time.sleep(3)
