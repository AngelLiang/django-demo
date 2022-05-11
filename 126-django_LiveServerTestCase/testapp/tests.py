from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from django.contrib.auth import get_user_model
User = get_user_model()

class MySeleniumTests(StaticLiveServerTestCase):
    # fixtures = ['user-data.json']

    # @classmethod
    # def setUpTestData(cls):
    #     # Set up data for the whole TestCase
    #     cls.testuser = User.objects.create_user(username='test', password='test')

    # def setUp(self):
    #     testuser = User.objects.create_user(username='test', password='test')

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

        testuser = User.objects.create_user(username='test', password='test')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        timeout = 2
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('test')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test')
        self.selenium.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
        WebDriverWait(self.selenium, timeout).until(lambda driver: driver.find_element_by_xpath('//*[@id="site-name"]'))
