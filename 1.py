# -*- coding: UTF-8 -*-
from urllib import request
from lxml import etree

areas = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn']
def getTemplate(area):

    url="http://www.weather.com.cn/textFC/"+area+'.shtml'
    page = request.Request(url)
    page_info = request.urlopen(page).read().decode('utf-8')
    html = etree.HTML(page_info)
    items = html.xpath('//div[@class="conMidtab"][1]/div')
    for i in items:
        getInfo(i)
        print("-"*48,"\n")
def getInfo(items):
    items = items.xpath('table/tr')
    sum=0
    for item in items[2:-1]:

        if sum == 0:
            province = item.xpath('td[1]/a/text()')[0]
            mat = "{:^36}"
            print(mat.format(province),'\n'*2)
            mat = "{:8}\t{:4}\t{:8}\t{:4}\t{:4}"
            print(mat.format("城市", "天气", "风向", "风力", "最低气温"),'\n')
            city = item.xpath('td[2]/a/text()')[0]
            phenomena = item.xpath('td[6]/text()')[0]
            winddirection = item.xpath('td[7]/span/text()')[0]
            windpower = item.xpath('td[7]/span/text()')[1]
            Minimumtemp = item.xpath('td[8]/text()')[0]

        else:
            city = item.xpath('td[1]/a/text()')[0]
            phenomena = item.xpath('td[5]/text()')[0]
            winddirection = item.xpath('td[6]/span/text()')[0]
            windpower=item.xpath('td[6]/span/text()')[1]
            Minimumtemp=item.xpath('td[7]/text()')[0]
        mat = "{:8}\t{:4}\t{:8}\t{:4}\t{:4}"
        print(mat.format(city,phenomena,winddirection,windpower,Minimumtemp))
        sum += 1

for area in areas:
    getTemplate(area)



