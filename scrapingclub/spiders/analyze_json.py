import scrapy
import json
import re


class AnalyzeJSON(scrapy.Spider):
    name = "analyze_json"
    file_name = "data/analyze_json.json"
    start_urls = ["https://scrapingclub.com/exercise/detail_json/"]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        data = re.findall("var obj =(.+?);\n", response.body.decode("utf-8"), re.S)
        f = open(self.file_name, "w")
        f.write(json.dumps(data))
        f.close()
