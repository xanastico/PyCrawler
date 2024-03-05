
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['https://lisbon.craigslist.org/']
    start_urls = ['http://https://lisbon.craigslist.org/']

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        for title in titles: 
            yield{'Title': title}
