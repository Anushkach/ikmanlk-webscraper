import scrapy

class ikmanSpider(scrapy.Spider):
    name='ikman'
    start_urls=['https://ikman.lk/en/ads/sri-lanka/electronics?page={}'.format(i) for i in range(1, 6)]
    s=2 
    def parse(self,response):
        for products in response.css('li.normal--2QYVk.gtm-normal-ad'):
            yield{
                'title':products.css('a.card-link--3ssYv.gtm-ad-item h2.heading--2eONR.heading-2--1OnX8.title--3yncE.block--3v-Ow::text').get(),
                'price':products.css('div.price--3SnqI.color--t0tGX span::text').get().replace('Rs ',''),
                'location':products.css('div.description--2-ez3::text').get(),
                'link':products.css('a.card-link--3ssYv.gtm-ad-item').attrib['href']
            }
        
        if self.s <= 3:
            yield response.follow("https://ikman.lk/en/ads/sri-lanka/electronics?page="+str(self.s),callback=self.parse)
            self.s+=1
                

