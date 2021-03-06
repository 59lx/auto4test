from core.utils import Utils
from core.driver_handler import DriverHandler
import time
import os
# 羊驼cms Page 页面测试类
class YtLink(object):

    def __init__(self, driver, logger, url):
        self.driver = driver
        self.logger = logger
        self.url = url
        self.utils = Utils(self.driver, self.logger)

    def run(self):
        self.utils.get_item_and_click('//li[2]/a')
        self.driver.implicitly_wait(3)
        self.utils.get_item_and_click('//div/a')
        self.utils.insert_to_all_text()
        self.utils.get_item_and_click('//button[1]')

