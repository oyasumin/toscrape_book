# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BookItem(scrapy.Item):
    # 书名
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 评价等级，1~5星
    review_rating = scrapy.Field()
    # 评价数量
    review_num = scrapy.Field()
    # 产品编码
    upc = scrapy.Field()
    # 库存量
    stock = scrapy.Field()

class ToscrapeBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
