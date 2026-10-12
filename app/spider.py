import scrapy

class SupplierSpider(scrapy.Spider):
    name="supplier"
    start_urls=[]

    def parse(self,response):
        for card in response.css(".product"):
            yield {
                "name": card.css(".name::text").get(),
                "url": response.url,
                "price": card.css(".price::text").get()
            }
