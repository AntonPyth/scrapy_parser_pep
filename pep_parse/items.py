import scrapy


class PepParseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
