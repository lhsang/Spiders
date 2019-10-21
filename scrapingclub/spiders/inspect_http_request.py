import scrapy
import json


class InspectHttp(scrapy.Spider):
    name = "inspect_http_request"
    file_name = "data/inspect_http_request.json"
    start_urls = ["https://scrapingclub.com/exercise/ajaxdetail_header/"]

    # set headers in setting.py
    def parse(self, response):
        f = open(self.file_name, "w")
        f.write(json.dumps(json.loads(response.body)))
        f.close()
