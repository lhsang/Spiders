import scrapy
from loginform import fill_login_form
from . import getParamsFromCookie, getCookieFromResponse


class LoginForm(scrapy.Spider):
    name = 'login_form'
    login_url = "https://scrapingclub.com/exercise/basic_login/"
    acc = {
        "name": "scrapingclub",
        "password": "scrapingclub"
    }
    start_urls = ["https://scrapingclub.com/exercise/basic_login_check/"]
    cookie = None
    headers = {
        "origin": "https://scrapingclub.com",
        "referer": "https://scrapingclub.com/exercise/basic_login/",
        "content-type": "application/x-www-form-urlencoded"
    }

    @classmethod
    def start_crawl(self, response):
        print("You have successfully login in, Congratulations\n")
        print(response.body)

    def parse(self, response):
        if not self.cookie:
            self.cookie = getParamsFromCookie(getCookieFromResponse(response), ["csrftoken"])
            csrfmiddlewaretoken = response.css('form input').xpath('@value').get()
            return [scrapy.FormRequest("https://scrapingclub.com/exercise/basic_login/", formdata={
                'name': self.acc['name'],
                'password': self.acc['password'],
                'csrfmiddlewaretoken': csrfmiddlewaretoken
            }, callback=self.start_crawl, headers=self.headers)]
        else:
            print("============")
            print(response.body)
