import scrapy
import json

class FindGoldInCookie(scrapy.Spider):
    name = "find_gold_in_cookie"
    file_name = "data/find_gold_in_cookie.json"
    start_urls = ["https://scrapingclub.com/exercise/detail_cookie/"]
    cookie = None

    def parse(self, response):
        if not self.cookie:
            self.cookie = str(response.headers.getlist('Set-Cookie')[0]).split(';')
            print("============")
            print(self.cookie)
            print("=======")