# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst,MapCompose
from . import utils


class BolItem(scrapy.Item):

    productName = scrapy.Field(
       input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

    productID = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

