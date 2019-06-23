# -*- coding: utf-8 -*-

import scrapy
import json
import codecs


class GithubSpyder(scrapy.Spider):

    name = "github"

    def start_requests(self):
        urls = [
            "https://github.com/angular/angular"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        repository = {
            # 'author': response.css('a.author.js-popover>div.avatar').get(),
            'author': response.css('h1>span>a.url.fn::text').get(),
            'repository': response.css('h1>strong>a::text').get(),
            'Watch': response.css('a.social-count.js-social-count::text').get().strip(),
            'Watch': response.css('//*[@id="js-repo-pjax-container"]/div[1]/div/ul/li[2]/form/a').get().strip(),
            # 'category': response.xpath("//li//a//span[@property='name']//text()").getall()[1],
            # 'title': response.css('div>h1.title>a::text').get(),
            # 'author': max(response.xpath("//a[@class='author js-popover']//text()").getall()),
            # 'chapter' : response.css('h2.title::text').get(),
            # 'content': response.css('div.content#js-truyencv-content::text').getall()
        }

        self.log(chap)

        with codecs.open('chap_{}.json'.format(i), 'w', encoding='utf-8') as f:
            json.dump(chap, f, ensure_ascii=False)
            self.log("write to file chap_{}.json success".format(1))

