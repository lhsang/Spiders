import scrapy

class Basic(scrapy.Spider):
    name = "basic"

    def start_requests(self):
        urls = ["https://scrapingclub.com/exercise/detail_basic/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        for card in response.css('div.card'):
            body = card.css('div.card-body')
            yield {
                'title': body.css('h3.card-title::text').get(),
                'price': body.css('h4::text').get(),
                'decription': body.css('p.card-text::text').get()
            }
