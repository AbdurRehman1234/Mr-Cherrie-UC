# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FareastScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    High = scrapy.Field()
    Low = scrapy.Field()
    Volume = scrapy.Field()
    volume_bs = scrapy.Field()
    price = scrapy.Field()
    fiftytwoW = scrapy.Field()
    ROE = scrapy.Field()
    PE = scrapy.Field()
    EPS = scrapy.Field()
    DPS = scrapy.Field()
    DY = scrapy.Field()
    NTA = scrapy.Field()
    PB = scrapy.Field()
    RPS = scrapy.Field()
    PSR = scrapy.Field()
    Market_cap = scrapy.Field()
    Shares = scrapy.Field()
    RSI = scrapy.Field()
    Stochastic14 = scrapy.Field()
    Average3M = scrapy.Field()
    Relative_Volume = scrapy.Field()
    last_done = scrapy.Field()
    change = scrapy.Field()
    percent_change = scrapy.Field()

