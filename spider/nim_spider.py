import re
import scrapy
from scrapy.selector import HtmlXPathSelector

class NimSpider(scrapy.Spider):
    name = 'nim_spider'
    start_urls = ['https://six.akademik.itb.ac.id/publik/displayprodikelas.php?semester=2&tahun=2016&th_kur=2013']

    def parse(self, response):
        ITEM_SELECTOR = 'li'
        for link in response.css(ITEM_SELECTOR):

            NEXT_PAGE_SELECTOR = 'a ::attr(href)'
            next_page = link.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )

        if response.css('pre'):
            hxs = HtmlXPathSelector(response)
            hxs.select('//base/text()').extract()
            for line in hxs.select('//pre/text()').re(r'(.*)\n'):
                nim_line = re.search( r'[0-9]{3} *(\d{8}) *(.+)', line)
                if(nim_line!=None):
                    yield {
                        "nim" : nim_line.group(1),
                        "name" : nim_line.group(2).rstrip(),
                    }