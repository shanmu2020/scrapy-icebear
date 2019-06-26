# -*- coding: utf-8 -*-
import scrapy
from icebear.items import IcebearItem


class icebearSpider(scrapy.Spider):
    name = 'icebear'
    allowed_domains = ['icebear.me']
    host = 'https://icebear.me'
    # start_urls = [('%s/job.html' % host)]
    start_urls = [('%s/job' % host)]
    now_page = 0

    def parse(self, response):
        self.now_page = self.now_page + 1
        data = dict(filter="0!0!0!0!0!0!!1", page=str(self.now_page))
        yield scrapy.FormRequest(url=self.start_urls[0], method="POST", formdata=data, callback=self.parse_data)

    def parse_data(self, response):
        with open('ice.html', 'wb') as f:
            f.write(response.body)
            f.flush()
        print(response.status)

    # def parse(self, response):
    #     print(response.url)
    #     with open("data.html",'w', encoding='utf-8') as f:
    #         f.write(str(response.body))
    #         f.close()
    #     li_list = response.xpath("//li[@class='comItem']/div")
    #     for li in li_list:
    #         item = IcebearItem()
    #         item['href'] = li.xpath("./a[1]/@href").extract_first()
    #         print(item['href'])
    #         yield item
