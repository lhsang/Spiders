import scrapy
import json

from . import getParamsFromCookie, getCookieFromResponse


class FindGoldInCookie(scrapy.Spider):
    name = "find_gold_in_cookie"
    file_name = "data/find_gold_in_cookie.json"
    start_urls = ["https://scrapingclub.com/exercise/detail_cookie/"]
    data_url = "https://scrapingclub.com/exercise/ajaxdetail_cookie/"
    token = None
    headers = {
        'referer': 'https://scrapingclub.com/',
        'X-Requested-With': 'XMLHttpRequest'
    }

    def parse(self, response):
        if not self.token:
            params = getParamsFromCookie(getCookieFromResponse(response), ['token'])
            self.token = params['token']
            request = scrapy.Request(url=self.data_url + '?token={}'.format(self.token), headers=self.headers)
            return request
        else:
            f = open(self.file_name, "w")
            f.write(json.dumps(json.loads(response.body)))
            f.close()
