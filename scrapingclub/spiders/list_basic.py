import scrapy
from scrapy.spiders import Rule, CrawlSpider
import re
import json
from . import isNullObj


class ScrapyPage(CrawlSpider):
    name = "list_basic"
    start_urls = [
        "https://scrapingclub.com/exercise/list_basic/?page=1"
    ]
    curr_page = 1
    result = []

    @classmethod
    def isContinue(self, response):
        paginations = response.css('.pagination li.page-item a.page-link::text').getall()
        for page in paginations:
            if page == 'Next':
                return True
        return False

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        for card in response.css('div.card'):
            body = card.css('div.card-body')
            obj = {
                'title': body.css('h4.card-title a::text').get(),
                'price': body.css('h5::text').get()
            }
            if not isNullObj(obj):
                self.result.append(obj)

        if self.isContinue(response):
            self.curr_page += 1
            next_page = re.sub(r'page=[0-9]*', 'page=' + str(self.curr_page), self.start_urls[0])
            yield response.follow(next_page, callback=self.parse)
        else:
            f = open('data/list_basic.json', 'w')
            f.write(json.dumps(self.result))
            f.close()
