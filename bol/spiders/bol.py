# -*- coding: utf-8 -*-
import scrapy
from .. import utils
from scrapy.loader import ItemLoader
from ..items import BolItem 
import logging

class BolSpider(scrapy.Spider):
    name = 'bol'
    allowed_domains = ['bol.com']
    start_urls = utils.start_urls

    def parse(self, response):
        response.selector.remove_namespaces()
        bulkmaps = response.xpath('//loc/text()')
        
        for sitemap_url in bulkmaps:
            yield scrapy.Request(url=sitemap_url.get(),
                                 callback=self.parse_sitemaps, 
                                 meta={
                                     'sitemap_len': len(bulkmaps)
                                })


    def parse_sitemaps(self,response):
        sitemap_len = response.request.meta['sitemap_len']
        response.selector.remove_namespaces()
        sitemaps = response.xpath('//loc/text()')
        for site in sitemaps:
            productLoader = ItemLoader(item=BolItem(), response=response)
            productLoader.add_value('productID', site.get().split('/')[-2].split('/')[0])
            productLoader.add_value('productName', site.get().split('/')[-3].split('/')[0])
            item = productLoader.load_item()
            yield item

   