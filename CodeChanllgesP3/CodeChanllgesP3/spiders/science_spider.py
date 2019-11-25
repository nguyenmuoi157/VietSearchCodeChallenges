import codecs
import json
import os
import os.path

import numpy as np
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "science"
    start_urls = [
        'https://vnexpress.net/khoa-hoc',
    ]

    def parse(self, response):
        for post in response.css('article.list_news'):
            link = post.css('h4.title_news a::attr(href)').re(r'https:\/\/.+html')[0]
            yield scrapy.Request(link, callback=self.parse_post_content)

        next_page = response.css('#pagination a.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_post_content(self, response):
        try:
            content = response.css("body section.container section.wrap_sidebar_12 section.sidebar_1")
            post = {
                "title": content.css("h1::text").get(),
                "content": content.css("article").get(),
                "published_date": content.css("header span.time::text").get()
            }
            if post["title"] is not None:
                self.write_json(post)
        except NameError:
            pass
        

    def write_json(self, post):
        list_post = np.array([])
        if os.path.exists("science.json"):
            with open("science.json", "r", encoding="utf8") as fr:
                json_data = fr.read()
                if json_data != '':
                    posts = json.loads(json_data)
                    list_post = np.array(posts)
                    duplicate_check = list_post[[x["title"] == post["title"] for x in list_post]]
                    if len(duplicate_check) == 0:
                        list_post = np.append(list_post, post)
                else:
                    list_post = np.array([post])
        data_list = list_post.tolist()
        with open("science.json", 'w', encoding='utf8') as fw:
            json.dump(data_list, fw, separators=(',', ':'), sort_keys=True, indent=4)
