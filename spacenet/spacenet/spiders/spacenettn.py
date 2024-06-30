import scrapy
from scrapy.http import Request
import datetime

class SpacenettnSpider(scrapy.Spider):
    name = "spacenettn"
    allowed_domains = ["spacenet.tn"]
    start_urls = ["https://spacenet.tn/13-smartphone-mobile-tunisie"]

    def parse(self, response):
        ad_title = [title.strip() for title in response.xpath('//*[@id="box-product-grid"]/div/div[*]/div/div[2]/h2/a/text()').extract()]
        ad_price = [price.strip() for price in response.xpath('//*[@id="box-product-grid"]/div/div[*]/div/div[2]/div[@class="product-price-and-shipping"]/span[@class="price"]/text()').extract()]
        ad_stocks = [stock.strip() for stock in response.xpath('//*[@id="box-product-grid"]/div/div[*]/div/div[2]/div[@class="button-action-bottom"]/div/div/label/text()').extract()]
        ad_href=response.xpath('//*[@id="box-product-grid"]/div/div[*]/div/div[2]/h2/a/@href').extract()
        date_current = datetime.datetime.now()
         # Stockage des données extraites
        for url, title, price, stock in zip(ad_href, ad_title, ad_price, ad_stocks):
            if url and title and price and stock:
                yield {
            'ad_url': url,
            'ad_title': title.encode('utf-8').decode('utf-8'),
            'ad_price': price.encode('utf-8').decode('utf-8'),
            'ad_stocks': stock.encode('utf-8').decode('utf-8'),
            'ad_website': response.url,
            'date_scrapy': date_current
        }

        # Extraction du lien de la page suivante
        next_page = response.xpath('//*[@id="js-product-list"]/nav/div/div/ul/li/a[@class="next js-search-link"]/@href').extract_first()
        
        if next_page:
            # Suivi du lien de la page suivante
            yield Request(url=next_page, callback=self.parse)
