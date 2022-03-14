import os

from src.crawler.crawler import DouyinCrawler
from src.util.reader import read_list


def main():
    crawler = DouyinCrawler("/home/xdrag/tools/chromedriver")
    crawler.open("https://www.douyin.com")
    crawler.login()
    print("Login success")
    crawler.to_search()

    search_keywords = read_list("../region.txt")
    for keyword in search_keywords:
        if keyword + '.csv' in os.listdir('../data'):
            continue
        crawler.search(keyword)
        crawler.scroll_down_until("div.Bllv0dx6")
        all_users = crawler.get_all_user(lambda u: u.nfans > 100000)
        with open(f"../data/{keyword}.csv", "w") as f:
            f.writelines(all_users)
    crawler.close()


if __name__ == '__main__':
    main()
