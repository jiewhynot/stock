# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from openpyxl import Workbook
class StocklistPipeline(object):
    def __init__(self):
        self.wb=Workbook()
        self.ws=self.wb.active
        self.ws.append(["股票代码", "股票价格"])
    def process_item(self, item, spider):


        line=[item["data"],item["price"]]
        self.ws.append(line)
        self.wb.save(r"C:\Users\jie1994\Desktop\yueshi\stock.xlsx")


    # def __init__(self):
    #     self.f=open('xici,json','wb')
    # def process_item(self,item,spider):
    #     text=json.dumps(dict(item),ensure_ascii=False)+',\n'
    #     self.f.write(text.encode('utf-8'))
    # def close_spider(self,spider):
    #     self.f.close()