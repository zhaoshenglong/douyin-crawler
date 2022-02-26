import time

from src.crawler.crawler import DouyinCrawler
from selenium import webdriver

KEYWORDS = ["亚洲"]


def main():
    crawler = DouyinCrawler("/home/xdrag/tools/chromedriver")
    crawler.open("https://www.douyin.com")
    crawler.login()
    print("Login success")
    crawler.to_search()
    for keyword in KEYWORDS:
        crawler.search(keyword)
        crawler.scroll_down_until("div.Bllv0dx6")
        all_users = crawler.get_all_user(lambda u: u.nfans > 100000)
        with open(f"{keyword}_data.csv", "w") as f:
            f.writelines(all_users)
    crawler.close()


if __name__ == '__main__':
    main()
