# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\10\9 0009 16:10$'

"""
PM25数据接口
"""

import requests
from lxml import etree
from requests.exceptions import RequestException
from multiprocessing import Pool

import os,django
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pm25project.settings")
django.setup()

from pm25.models import pm25



def get_html(url):
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 55.0.2883.87Safari / 537.36'
    }
    try:
        html = requests.get(url,headers=headers)
        if html.status_code == 200:
            html.encoding = "utf-8"
            return html.text
        return None
    except RequestException:
        return None


def get_city_name(url):
    html = get_html(url)
    xpath_info = etree.HTML(html)
    infos = xpath_info.xpath('//ul[@class="unstyled"]/div[2]/li')
    for info in infos:
        url = info.xpath('a/@href')[0]

        yield {
            'url':url
        }


def get_info(url):
    aqi_list = []
    html = get_html(url)
    sel = etree.HTML(html)
    aqi = sel.xpath('//div[@class="span1"]/div[1]/text()')[0].strip()
    aqi_list.append(aqi)

    city_name = sel.xpath('//div[@class="city_name"]/h2/text()')[0].strip()
    aqi_list.append(city_name)

    affect = sel.xpath('//div[@class="affect"]/p/text()')[0].strip()
    aqi_list.append(affect)

    action = sel.xpath('//div[@class="action"]/p/text()')[0].strip()
    aqi_list.append(action)

    level = sel.xpath('//div[@class="level"]/h4/text()')[0].strip()
    aqi_list.append(level)

    return aqi_list


def main():
    NUMBER = 0 # 计算器
    url = 'http://www.pm25.in/'
    for i in get_city_name(url):

        city_name_url = i.get('url')
        url = 'http://www.pm25.in/{}'.format(city_name_url)
        aqi = get_info(url)
        NUMBER += 1
        if NUMBER % 10 == 0:
            print("已经存储{}条数据".format(NUMBER))

        pm25_model = pm25.objects.create(city_name=aqi[1],pm25_value=int(aqi[0]),adive=aqi[2],step=aqi[3],grade=aqi[4])
        pm25_model.save()





if __name__ == '__main__':
    pool = Pool()
    try:
        pool.map(main())
    except:
        print("已经爬取完成")