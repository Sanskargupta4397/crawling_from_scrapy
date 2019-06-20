# -*- coding: utf-8 -*-
import scrapy
from crawl_amazon_smartphones.items import CrawlAmazonSmartphonesItem

class AmazonSmartphonesSpider(scrapy.Spider):
    name = 'amazon_smartphones'
    page_number=2
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.in/s?k=smartphones&page=2&qid=1560987333&ref=sr_pg_2']

    def parse(self, response):

        item = CrawlAmazonSmartphonesItem()

        for change in response.css('div.sg-row'):

            product_name = change.css('.a-color-base.a-text-normal::text').extract_first()
            product_price = change.css('.a-price-whole::text').extract_first()
            product_reviews = change.css('.a-icon-alt::text').extract_first()
            product_imglink = change.css('img.s-image::attr(src)').extract_first()


            item['product_name'] = product_name
            item['product_price'] = product_price
            item['product_reviews'] = product_reviews
            item['product_imglink'] = product_imglink


            yield item

        next_page_url = 'https://www.amazon.in/s?k=smartphones&page=' + str(AmazonSmartphonesSpider.page_number) + '&qid=1560987333&ref=sr_pg_' + str(AmazonSmartphonesSpider.page_number)
        print("Hi this is new url  :    ", next_page_url)
        if AmazonSmartphonesSpider.page_number is not None:
            AmazonSmartphonesSpider.page_number += 1
            yield response.follow(next_page_url, callback=self.parse)

