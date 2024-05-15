import scrapy



class ScrapingBooksTestSpider(scrapy.Spider):
    name = "scraping_books_test"
    
    def start_requests(self):
        URL = 'https://books.toscrape.com/'
        yield scrapy.Request(url=URL, callback=self.response_parser)

    def response_parser(self, response):
        for selector in response.css('article.product_pod'):
            yield {
                'title': selector.css('h3 > a::attr(title)').extract_first(),
                'price': selector.css('.price_color::text').extract_first()
            }

        # next_page_link = response.css('li.next a::attr(href)').extract_first()
        # if next_page_link:
        #     yield response.follow(next_page_link, callback=self.response_parser)
