import scrapy
import csv
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher


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

        next_page_link = response.css('li.next a::attr(href)').extract_first()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)

def scraping_result():
    book_results = []

    def crawler_results(item):
        book_results.append(item)

    dispatcher.connect(crawler_results, signal = signals.item_scraped)
    crawler_process = CrawlerProcess()
    crawler_process.crawl(ScrapingBooksTestSpider)
    crawler_process.start()
    return book_results

def run():
    book_data = scraping_result()
    return book_data

if __name__ == '__main__':
    book_data = run()
    for item in book_data:
        print(f"Title: {item['title']}, Price: {item['price']}")


