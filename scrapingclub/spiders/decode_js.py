import scrapy
from scrapy_splash import SplashRequest
from . import isNullObj


class DecodeJS(scrapy.Spider):
    start_urls = ["https://scrapingclub.com/exercise/detail_sign/"]
    name = 'decode_js'
    result = []

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 1})

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        for card in response.css('div.card'):
            body = card.css('div.card-body')
            obj = {
                'title': body.css('.card-title::text').get(),
                'price': body.css('.card-price::text').get(),
                'decription': body.css('p.card-description::text').get()
            }
            if not isNullObj(obj):
                self.result.append(obj)
        print(self.result)