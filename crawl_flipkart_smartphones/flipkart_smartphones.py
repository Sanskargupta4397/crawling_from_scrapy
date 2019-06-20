# -*- coding: utf-8 -*-
import scrapy
from crawl_flipkart_smartphones.items import CrawlFlipkartSmartphonesItem

class FlipkartSmartphonesSpider(scrapy.Spider):

    name = 'flipkart_smartphones'
    page_number = 1
    allowed_domains = ['flipkart.com']
    start_urls = ['https://www.flipkart.com/search?q=smart+phones&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_5&otracker1=AS_QueryStore_HistoryAutoSuggest_1_5&as-pos=1&as-type=HISTORY&as-backfill=on&page=1']

    def parse(self, response):

        item = CrawlFlipkartSmartphonesItem()

        for change in response.css('div.bhgxx2'):
            product_name = change.css('div._3wU53n::text').extract_first()
            product_price = change.css('div._2rQ-NK::text').extract_first()
            product_rating= change.css('div.hGSR34::text').extract_first()




            item['product_name'] = product_name
            item['product_price'] = product_price
            item['product_rating'] = product_rating


            yield item


        next_page_url = 'https://www.flipkart.com/search?q=smart+phones&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_5&otracker1=AS_QueryStore_HistoryAutoSuggest_1_5&as-pos=1&as-type=HISTORY&as-backfill=on&page=' +str(FlipkartSmartphonesSpider.page_number)
        print("Hi this is new url  :    ", next_page_url)
        if FlipkartSmartphonesSpider.page_number is not None:
            FlipkartSmartphonesSpider.page_number += 1
            yield response.follow(next_page_url, callback=self.parse)
