# First, we need to update our discover_product_urls() method to extract all
# the product URLs from the search_products and then send a request to
# each one.
import json
import scrapy
from urllib.parse import urljoin
import re

class AmazonSearchProductSpider(scrapy.Spider):
    name = "amazon_search_product"

    def start_requests(self):
        keyword_list = ['ipad']
        for keyword in keyword_list:
            amazon_search_url = f'https://www.amazon.com/s?k={keyword}&page=1'
            yield scrapy.Request(url=amazon_search_url, callback=self.discover_product_urls, meta={'keyword': keyword, 'page': 1})

    def discover_product_urls(self, response):
        page = response.meta['page']
        keyword = response.meta['keyword'] 

        ## Discover Product URLs
        search_products = response.css("div.s-result-item[data-component-type=s-search-result]")
        for product in search_products:
            relative_url = product.css("h2>a::attr(href)").get()
            product_url = urljoin('https://www.amazon.com/', relative_url).split("?")[0]
            yield scrapy.Request(url=product_url, callback=self.parse_product_data, meta={'keyword': keyword, 'page': page})
            
        ## Get All Pages
        if page == 1:
            available_pages = response.xpath(
                '//*[contains(@class, "s-pagination-item")][not(has-class("s-pagination-separator"))]/text()'
            ).getall()

            last_page = available_pages[-1]
            for page_num in range(2, int(last_page)):
                amazon_search_url = f'https://www.amazon.com/s?k={keyword}&page={page_num}'
                yield scrapy.Request(url=amazon_search_url, callback=self.parse_search_results, meta={'keyword': keyword, 'page': page_num})


    def parse_product_data(self, response):
        ## Add product data extraction code here
        pass

    # This will extract all the URLs from the Amazon search page, request
    # the URL and then trigger a parse_product_data scraper when it recieves
    # a response.
    
