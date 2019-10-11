import scrapy
import json


class InspectHttp(scrapy.Spider):
    name = "inspect_http_request"
    file_name = "data/inspect_http-request.json"
    start_urls = ["https://scrapingclub.com/exercise/ajaxdetail_header/"]
    headers = {
        'referer': 'https://scrapingclub.com/',
        'X-Requested-With': 'XMLHttpRequest'
    }

    def start_requests(self):
        requests = []
        for url in self.start_urls:
            requests.append(scrapy.Request(url=url, headers=self.headers))
        return requests

    def parse(self, response):
        f = open(self.file_name, "w")
        f.write(json.dumps(json.loads(response.body)))
        f.close()
