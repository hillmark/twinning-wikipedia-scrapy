import scrapy

from twinning.items import TwinningItem
from twinning.utils import snake_case

class TwinningSpider(scrapy.Spider):
    name = 'twinning'
    allowed_domains = ['wikipedia.org']
    base_url = 'https://en.wikipedia.org'

    def start_requests(self):
        url = self.base_url + '/wiki/List_of_twin_towns_and_sister_cities_in_England'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        towns = response.xpath('//h2/span[@id="A"]/parent::h2//following-sibling::*//li/span[@class="flagicon"]/parent::li')
        for town_b in towns:
            town_a = town_b.xpath('ancestor::*/preceding-sibling::p[1]')
            item = TwinningItem()
            item['town_a_name'] = town_a.xpath('b/a/text()').get()
            item['town_a_url'] = self.base_url + town_a.xpath('b/a/@href').get()
            item['town_a_country'] = 'England'
            item['town_b_name'] = town_b.xpath('a/text()').get()
            item['town_b_url'] = self.base_url + town_b.xpath('a/@href').get()
            item['town_b_country'] = ''.join(town_b.xpath('text()').getall()).replace(' , ', '')
            item['id'] = snake_case(item['town_a_name'] + '_' + item['town_b_name'])
            yield item
