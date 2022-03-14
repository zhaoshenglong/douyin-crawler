from src.util.number import text_to_num
from selenium.webdriver.remote.webelement import WebElement


class DouyinUser:
    def __init__(self, user_ele: WebElement):
        homepage_ele = user_ele.find_element_by_css_selector("a[href*='www.douyin.com/user']")
        self.__homepage = homepage_ele.get_attribute("href")
        name_box = user_ele.find_element_by_class_name("RBOV8jrE")
        name_ele = name_box.find_element_by_class_name("bMoJi1wE")
        self.__name = name_ele.text
        try:
            location_ele = name_box.find_element_by_class_name("vXvSqSN8")
            self.__location = location_ele.text
        except Exception as e:
            self.__location = "未知"
        stat_box: WebElement = user_ele.find_element_by_class_name("H7Xy0nwI")
        stat_span_list = stat_box.find_elements_by_tag_name("span")
        for stat_span_ele in stat_span_list:
            if "获赞" in stat_span_ele.text:
                self.__nlikes = text_to_num(stat_span_ele.text)
            if "粉丝" in stat_span_ele.text:
                self.__nfans = text_to_num(stat_span_ele.text)
        sign_box = user_ele.find_element_by_class_name("go5cmngM")
        self.__signature = sign_box.text

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def nfans(self):
        return self.__nfans

    @nfans.setter
    def nfans(self, nfans):
        self.__nfans = nfans

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def signature(self):
        return self.__signature

    @signature.setter
    def signature(self, signature):
        self.__signature = signature

    @property
    def nlikes(self):
        return self.__nlikes

    @nlikes.setter
    def nlikes(self, nlikes):
        self.__nlikes = nlikes

    @property
    def homepage(self):
        return self.__homepage

    def __repr__(self):
        return f"DouyinUser(" \
               f"name={self.__name}," \
               f"location={self.__location}," \
               f"signature={self.__signature}," \
               f"nlikes={self.__nlikes}," \
               f"nfans={self.__nfans})"

    def __str__(self):
        return f"{self.__name}," \
               f"{self.__nlikes}," \
               f"{self.__nfans}," \
               f"{self.__location}," \
               f"{self.__signature}\n"
