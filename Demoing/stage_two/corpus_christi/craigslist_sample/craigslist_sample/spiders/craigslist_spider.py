

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

class CraigslistSpider(CrawlSpider):
    name = "craigslist"
    allowed_domains = ["craigslist.org"]
    start_urls = [
		 "http://corpuschristi.craigslist.org",
		 "http://corpuschristi.craigslist.org/cas/",
		 "http://corpuschristi.craigslist.org/cas/index100.html",
		 "http://corpuschristi.craigslist.org/cas/index200.html",
		 "http://corpuschristi.craigslist.org/cas/index300.html",
		 "http://corpuschristi.craigslist.org/cas/index400.html",
		 "http://corpuschristi.craigslist.org/cas/index500.html",
		 "http://corpuschristi.craigslist.org/cas/index600.html",
		 "http://corpuschristi.craigslist.org/cas/index700.html",
		 "http://corpuschristi.craigslist.org/cas/index800.html",
		 "http://corpuschristi.craigslist.org/cas/index900.html",
		 "http://corpuschristi.craigslist.org/cas/index1000.html",
		 "http://corpuschristi.craigslist.org/cas/index1100.html",
		 "http://corpuschristi.craigslist.org/cas/index1200.html",
		 "http://corpuschristi.craigslist.org/cas/index1300.html",
		 "http://corpuschristi.craigslist.org/cas/index1400.html",
		 "http://corpuschristi.craigslist.org/cas/index1500.html",
		 "http://corpuschristi.craigslist.org/cas/index1600.html",
		 "http://corpuschristi.craigslist.org/cas/index1700.html",
		 "http://corpuschristi.craigslist.org/cas/index1800.html",
		 "http://corpuschristi.craigslist.org/cas/index1900.html",
		 "http://corpuschristi.craigslist.org/cas/index2000.html",
		 "http://corpuschristi.craigslist.org/cas/index2100.html",
		 "http://corpuschristi.craigslist.org/cas/index2200.html",
		 "http://corpuschristi.craigslist.org/cas/index2300.html",
		 "http://corpuschristi.craigslist.org/cas/index2400.html",
		 "http://corpuschristi.craigslist.org/cas/index2500.html",
		 "http://corpuschristi.craigslist.org/cas/index2600.html",
		 "http://corpuschristi.craigslist.org/cas/index2700.html",
		 "http://corpuschristi.craigslist.org/cas/index2800.html",
		 "http://corpuschristi.craigslist.org/cas/index2900.html",
		 "http://corpuschristi.craigslist.org/cas/index3000.html",
		 "http://corpuschristi.craigslist.org/cas/index3100.html",
		 "http://corpuschristi.craigslist.org/cas/index3200.html",
		 "http://corpuschristi.craigslist.org/cas/index3300.html",
		 "http://corpuschristi.craigslist.org/cas/index3400.html",
		 "http://corpuschristi.craigslist.org/cas/index3500.html",
		 "http://corpuschristi.craigslist.org/cas/index3600.html",
		 "http://corpuschristi.craigslist.org/cas/index3700.html",
		 "http://corpuschristi.craigslist.org/cas/index3800.html",
		 "http://corpuschristi.craigslist.org/cas/index3900.html",
		 "http://corpuschristi.craigslist.org/cas/index4000.html",
		 "http://corpuschristi.craigslist.org/cas/index4100.html",
		 "http://corpuschristi.craigslist.org/cas/index4200.html",
		 "http://corpuschristi.craigslist.org/cas/index4300.html",
		 "http://corpuschristi.craigslist.org/cas/index4400.html",
		 "http://corpuschristi.craigslist.org/cas/index4500.html",
		 "http://corpuschristi.craigslist.org/cas/index4600.html",
		 "http://corpuschristi.craigslist.org/cas/index4700.html",
		 "http://corpuschristi.craigslist.org/cas/index4800.html",
		 "http://corpuschristi.craigslist.org/cas/index4900.html",
		 "http://corpuschristi.craigslist.org/cas/index5000.html",
		 "http://corpuschristi.craigslist.org/cas/index5100.html",
		 "http://corpuschristi.craigslist.org/cas/index5200.html",
		 "http://corpuschristi.craigslist.org/cas/index5300.html",
		 "http://corpuschristi.craigslist.org/cas/index5400.html",
		 "http://corpuschristi.craigslist.org/cas/index5500.html",
		 "http://corpuschristi.craigslist.org/cas/index5600.html",
		 "http://corpuschristi.craigslist.org/cas/index5700.html",
		 "http://corpuschristi.craigslist.org/cas/index5800.html",
		 "http://corpuschristi.craigslist.org/cas/index5900.html",
		 "http://corpuschristi.craigslist.org/cas/index6000.html",
		 "http://corpuschristi.craigslist.org/cas/index6100.html",
		 "http://corpuschristi.craigslist.org/cas/index6200.html",
		 "http://corpuschristi.craigslist.org/cas/index6300.html",
		 "http://corpuschristi.craigslist.org/cas/index6400.html",
		 "http://corpuschristi.craigslist.org/cas/index6500.html",
		 "http://corpuschristi.craigslist.org/cas/index6600.html",
		 "http://corpuschristi.craigslist.org/cas/index6700.html",
		 "http://corpuschristi.craigslist.org/cas/index6800.html",
		 "http://corpuschristi.craigslist.org/cas/index6900.html",
		 "http://corpuschristi.craigslist.org/cas/index7000.html",
		 "http://corpuschristi.craigslist.org/cas/index7100.html",
		 "http://corpuschristi.craigslist.org/cas/index7200.html",
		 "http://corpuschristi.craigslist.org/cas/index7300.html",
		 "http://corpuschristi.craigslist.org/cas/index7400.html",
		 "http://corpuschristi.craigslist.org/cas/index7500.html",
		 "http://corpuschristi.craigslist.org/cas/index7600.html",
		 "http://corpuschristi.craigslist.org/cas/index7700.html",
		 "http://corpuschristi.craigslist.org/cas/index7800.html",
		 "http://corpuschristi.craigslist.org/cas/index7900.html",
		 "http://corpuschristi.craigslist.org/cas/index8000.html",
		 "http://corpuschristi.craigslist.org/cas/index8100.html",
		 "http://corpuschristi.craigslist.org/cas/index8200.html",
		 "http://corpuschristi.craigslist.org/cas/index8300.html",
		 "http://corpuschristi.craigslist.org/cas/index8400.html",
		 "http://corpuschristi.craigslist.org/cas/index8500.html",
		 "http://corpuschristi.craigslist.org/cas/index8600.html",
		 "http://corpuschristi.craigslist.org/cas/index8700.html",
		 "http://corpuschristi.craigslist.org/cas/index8800.html",
		 "http://corpuschristi.craigslist.org/cas/index8900.html",
		 "http://corpuschristi.craigslist.org/cas/index9000.html",
		 "http://corpuschristi.craigslist.org/cas/index9100.html",
		 "http://corpuschristi.craigslist.org/cas/index9200.html",
		 "http://corpuschristi.craigslist.org/cas/index9300.html",
		 "http://corpuschristi.craigslist.org/cas/index9400.html",
		 "http://corpuschristi.craigslist.org/cas/index9500.html",
		 "http://corpuschristi.craigslist.org/cas/index9600.html",
		 "http://corpuschristi.craigslist.org/cas/index9700.html",
		 "http://corpuschristi.craigslist.org/cas/index9800.html",
		 "http://corpuschristi.craigslist.org/cas/index9900.html"
 
]
    rules = (Rule(SgmlLinkExtractor(allow=(),restrict_xpaths=('//a')), callback="parse", follow= True),)

    def parse(self, response):
      hxs = HtmlXPathSelector(response)
      titles = hxs.select("//span[@class='pl']")
      date_info = hxs.select("//h4[@class='ban']/span[@class='bantext']/text()")
      items = []
      file_to = open("things.txt","a")
      file_to.write(response.body)
      for titles in titles:
          item = CraigslistSampleItem()
          item ["title"] = titles.select("a/text()").extract()
          item ["link"] = titles.select("a/@href").extract()
          item ["date"] = date_info.extract()
          items.append(item)
      return items


