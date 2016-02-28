# -*- coding: utf-8 -*-
import scrapy

import pdb
from crawlapp.items import CrawlappItem


def get_item(item):
    if item and isinstance(item, list):
        return item[0]
    else:
        return ''


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = (
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/',
        'http://www.dmoz.org/Computers/Programming/Languages/Ruby/Books/',
        'http://www.dmoz.org/Computers/Programming/Languages/Ruby/Articles/',
    )


    def parse(self, response):
        item_list = response.xpath('//ul[@class="directory-url"]/li')
        for data in item_list:
            yield self.parse_item(data, response)


    def parse_item(self, data, response):
        item = CrawlappItem()
        item['title'] = get_item(data.xpath('a/text()').extract())
        item['link'] = get_item(data.xpath('a/@href').extract())
        item['desc'] = ''.join(data.xpath('text()').extract()).strip()
        return item
