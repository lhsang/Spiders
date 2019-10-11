import scrapy
import json

class InspectHttp(scrapy.Spider):
    name = "inspect_http_request"
    file_name = "data/inspect_http-request.json"
    start_urls = ["https://scrapingclub.com/exercise/ajaxdetail_header/"]


    def start_requests(self):
        requests = []
        for url in self.start_urls:
            requests.append(scrapy.Request(url=url, headers={'Referer': 'https://scrapingclub.com/exercise/detail_header/'}))
        return requests

    def parse(self, response):
        print("---------------")
        print(response.body)
        print("-------------------")