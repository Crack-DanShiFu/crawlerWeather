# -*- coding: UTF-8 -*-

from urllib import request
from lxml import etree

def getTemplate():

    url="http://www.weather.com.cn/textFC/"+'gat.shtml'
    page = request.Request(url)
    page_info = request.urlopen(page).read().decode('utf-8')
    html = etree.HTML(page_info)
    items = html.xpath('//div[@class="conMidtab"]/div')
    gat = items[0].xpath('table/tr[3]/td/a/text()')
    print(gat)

getTemplate()

