# -*- coding: utf-8 -*-

import scrapy
import json
import codecs


class TruyemCVSpider(scrapy.Spider):

    name = "truyencv"

    def start_requests(self):
        urls = [
            "https://truyencv.com/van-co-de-nhat-tong/chuong-1/"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'truyencv-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

        i = 1

        chap = {
            # 'author': response.css('a.author.js-popover>div.avatar').get(),
            'title': response.css('div>h1.title>a::text').get(),
            'author': max(response.xpath("//a[@class='author js-popover']//text()").getall()),
            'chapter' : response.css('h2.title::text').get(),
            'content': response.css('div.content#js-truyencv-content::text').getall()
        }

        self.log(chap)

        with codecs.open('chap_{}.json'.format(i), 'w', encoding='utf-8') as f:
            json.dump(chap, f, ensure_ascii=False)
            self.log("write to file chap_{}.json success".format(1))

