# -*- coding: UTF-8 -*-

from urllib import request
from lxml import etree
from pyecharts import Bar
from pyecharts import Map

areas = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn','gat']
Template_List=[]
province_List=[]
province_aveTemp_List=[]

Min_List=[]

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
    s=0
    City_temp_List = []
    for item in items[2:-1]:
        if s == 0:
            province = item.xpath('td[1]/a/text()')[0]
            mat = "{:^36}"
            print(mat.format(province),'\n'*2)
            province_List.append(province)
            mat = "{:8}\t{:4}\t{:8}\t{:4}\t{:4}\t{:4}"
            print(mat.format("城市", "天气", "风向", "风力", "最低气温", "最高气温"),'\n')
            city = item.xpath('td[2]/a/text()')[0]
            phenomena = item.xpath('td[6]/text()')[0]
            winddirection = item.xpath('td[7]/span/text()')[0]
            windpower = item.xpath('td[7]/span/text()')[1]
            Maximumtemp=item.xpath('td[5]/text()')[0]
            Minimumtemp = item.xpath('td[8]/text()')[0]

        else:
            city = item.xpath('td[1]/a/text()')[0]
            phenomena = item.xpath('td[5]/text()')[0]
            winddirection = item.xpath('td[6]/span/text()')[0]
            windpower=item.xpath('td[6]/span/text()')[1]
            Maximumtemp=item.xpath('td[4]/text()')[0]
            Minimumtemp=item.xpath('td[7]/text()')[0]

        mat = "{:8}\t{:4}\t{:8}\t{:4}\t{:4}\t{:4}"
        print(mat.format(city,phenomena,winddirection,windpower,Minimumtemp,Maximumtemp))
        # City_temp_List.append((float(Maximumtemp)+float(Minimumtemp))/2)
        City_temp_List.append(float(Minimumtemp))
        s += 1

    province_aveTemp_List.append(sum(City_temp_List)/City_temp_List.__len__())

for area in areas:
    getTemplate(area)

value=province_aveTemp_List
attr=province_List
map=Map("Map 结合 VisualMap 示例",width=1200,height=600)
map.add("",attr,value,maptype='china',visual_range=[-30,40],is_visualmap=True,visual_text_color="#000")
map.render("map.html")