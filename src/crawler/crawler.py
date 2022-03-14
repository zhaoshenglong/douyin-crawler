import time
from enum import Enum

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.crawler.user import DouyinUser
from src.util.checker import *
from selenium import webdriver


class DouyinSearchType(Enum):
    GENERAL = "general"
    VIDEO = "video"
    USER = "user"
    LIVE = "live"


class DouyinCrawler:
    def __init__(self, driver_path):
        check_file_exists(driver_path)
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def open(self, url):
        if not url.startswith("http"):
            url = "https://" + url
        self.driver.get(url)
        self.driver.maximize_window()

    def login(self, username="user", password="123"):
        btn_selector = ".login-guide .login-guide__btn"
        login_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, btn_selector)))
        login_btn.click()

        # Wait at most 1 minute for login
        logout_selector = "退出登录"
        _ = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.LINK_TEXT, logout_selector)))

    def __get_search_input(self):
        search_selector = "input.igFQqPKs"
        search_form: WebElement = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, search_selector)))
        search_form.send_keys(Keys.CONTROL + 'a')
        search_form.send_keys(Keys.BACK_SPACE)
        return search_form

    def __get_search_btn(self):
        search_btn = "button[type='button']"
        search_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, search_btn)))
        return search_btn

    def to_search(self):
        search_form = self.__get_search_input()
        search_btn = self.__get_search_btn()
        search_form.send_keys("dummy")
        search_btn.click()
        while len(self.driver.window_handles) < 2:
            time.sleep(0.1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        # Make sure the page load ok
        time.sleep(1)

    def search(self, keyword, search_type=DouyinSearchType.USER):
        search_form = self.__get_search_input()
        search_form.send_keys(keyword)

        search_btn = self.__get_search_btn()
        search_btn.click()

        search_type_selector = f"span[data-key='{search_type.value}']"
        search_type_btn = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, search_type_selector)))
        search_type_btn.click()
        # Make sure the page load ok
        time.sleep(1)

    def scroll_down_until(self, css_selector):
        while True:
            self.driver.execute_script('window.scrollBy(0,500)')
            time.sleep(0.2)
            try:
                bottom_div = self.driver.find_elements_by_css_selector(css_selector)
                if len(bottom_div) > 0:
                    break
            except Exception as e:
                print(e)
            finally:
                time.sleep(0.5)

    def get_all_user(self, filter_user):
        user_selector = "li.aCTzxbOJ.OPn2NCBX"
        user_ele_list = self.driver.find_elements_by_css_selector(user_selector)
        user_list = []
        for user_ele in user_ele_list:
            user = DouyinUser(user_ele)
            if filter_user(user):
                user_list.append(str(user))
        return user_list

    def close(self):
        self.driver.close()
