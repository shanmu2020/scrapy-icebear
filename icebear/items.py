# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IcebearItem(scrapy.Item):
    # define the fields for your item here like:
    href = scrapy.Field()
    post = scrapy.Field()
    method = scrapy.Field()
    company = scrapy.Field()
    city = scrapy.Field()
    category = scrapy.Field()
