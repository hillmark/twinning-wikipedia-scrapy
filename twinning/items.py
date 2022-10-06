# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TwinningItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    town_a_name = scrapy.Field()
    town_a_url = scrapy.Field()
    town_a_country = scrapy.Field()
    town_b_name = scrapy.Field()
    town_b_url = scrapy.Field()
    town_b_country = scrapy.Field()