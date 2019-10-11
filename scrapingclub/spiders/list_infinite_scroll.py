import scrapy
import json
import re


class ListScroll(scrapy.Spider):
    name = "list_infinite_scroll"
    file_name = "data/list_infinite_scroll.json"
    start_urls = ["https://scrapingclub.com/exercise/list_infinite_scroll/?page=1"]
    curr_page = 1
    result = []

    @classmethod
    def isContinue(self, response):
        paginations = response.css('.pagination li.page-item a.page-link::text').getall()
        for page in paginations:
            if page == 'Next':
                return True
        return False

    @classmethod
    def isNullObj(self, obj):
        for key in obj:
            if obj[key] is not None:
                return False
        return True

    def parse(self, response):
        cards = response.css('.card')
        for card in cards:
            body = card.css('div.card-body')
            obj = {
                "title": body.css("h4.card-title a::text").get(),
                "price": body.css("h5::text").get()
            }
            if not self.isNullObj(obj):
                self.result.append(obj)

        if self.isContinue(response):
            self.curr_page += 1
            next_page = re.sub(r'page=[0-9]*', 'page=' + str(self.curr_page), self.start_urls[0])
            yield response.follow(next_page, callback=self.parse)
        else:
            f = open(self.file_name, 'w')
            f.write(json.dumps(self.result))
            f.close()
