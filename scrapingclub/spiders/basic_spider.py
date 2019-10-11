import scrapy
import json

class Basic(scrapy.Spider):
    name = "basic"
    start_urls = ["https://scrapingclub.com/exercise/detail_basic/"]
    result = []
    file_name = 'data/basic_spider.json'

    @classmethod
    def isNullObj(self, obj):
        for key in obj:
            if obj[key] is not None:
                return False
        return True

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        for card in response.css('div.card'):
            body = card.css('div.card-body')
            obj = {
                'title': body.css('h3.card-title::text').get(),
                'price': body.css('h4::text').get(),
                'decription': body.css('p.card-text::text').get()
            }
            if not self.isNullObj(obj):
                self.result.append(obj)
        f = open(self.file_name, "w")
        f.write(json.dumps(self.result))
        f.close()