# -*- coding: utf-8 -*-
import scrapy
import re
from stocklist.items import StocklistItem
from scrapy.http import Request



class StockSpider(scrapy.Spider):
    name = 'stock'
    # allowed_domains = ['eastmoney.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        stockdata=[]
        lilist1=response.xpath('//div[@id="quotesearch"]/ul[1]/li').extract()
        for i in lilist1:
            num=int(re.findall("\d+",i)[0])
            if num>580027 and num<900901:
                number="sh"+str(num)
                stockdata.append(number)

        lilist2=response.xpath('//div[@id="quotesearch"]/ul[2]/li').extract()
        for j in lilist2[0:1427]:
            num1= re.findall("\d+", j)[0]
            number1="sz"+num1
            stockdata.append(number1)
        for k in lilist2[2158:2894]:
            num2 = re.findall("\d+", k)[0]
            number2 = "sz" + num2
            stockdata.append(number2)

        for m in stockdata[0:100]:
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",

                "Referer": "https://gupiao.baidu.com/",

                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",

                }

            url="https://gupiao.baidu.com/stock/"+m+".html"
            yield scrapy.Request(url,callback=self.parse_item,headers=headers)
    def parse_item(self,response):

        price=response.xpath('//div[@id="app-wrap"]//strong/text()').extract()

        url=re.findall("(\d+)",response.url)[0]
        print(price[0])
        print(url)

        item=StocklistItem()
        item["price"]=price[0]
        item["data"]=url
        yield  item






