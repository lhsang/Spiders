import scrapy
import json


class MimickingAjax(scrapy.Spider):
    name = "mimicking_ajax_request"
    start_urls = ["https://scrapingclub.com/exercise/ajaxdetail/"]
    file_name = "data/mimicking_ajax.json"

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        f = open(self.file_name, "w")
        f.write(json.dumps(json.loads(response.body)))
