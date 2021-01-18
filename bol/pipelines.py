# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter
import os

class BolPipeline(object):

    def open_spider(self, spider):
        self.filesExported = {}

    def close_spider(self, spider):
        pass

    def exportItem(self, item):
        productID = item['productID']
        productName = item['productName']
        if not os.path.exists('output'):
            os.mkdir('output')
        if productID not in self.filesExported:
            f = open('output/'+productID+'.json', 'wb')
            exporter = JsonItemExporter(f)
            exporter.start_exporting()
            exporter.export_item(item)
            exporter.finish_exporting()
            f.close()
            self.filesExported[productID] = exporter
            return self.filesExported[productID]
        else:
            return None

    def process_item(self, item, spider):
        exporter = self.exportItem(item=item)
        return item
