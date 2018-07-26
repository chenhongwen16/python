#!/usr/bin/env python
#coding:utf-8

import scrapy
from scrapy.spider import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from doubanmovie.items import DoubanmovieItem

class Douban(CrawlSpider):
    name = "douban"
    start_urls = ["http://movie.douban.com/top250"]


    def parse(self, response):
        item = DoubanmovieItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMovie in Movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle =  ''
            for each in title:
                fullTitle += each
            movieInfo = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[0]
            critical = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[1]
            quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if(quote):
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo)
            item['star'] = star
            item['critical'] = critical
            item['quote'] = quote
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()

        if nextLink:
            nextLink = nextLink[0]
            print nextLink
            yield Request(self.url + nextLink,callback=self.parse)