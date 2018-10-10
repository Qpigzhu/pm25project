# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\10\10 0010 12:31$'

"""
IP定位接口 返回:城市名 参数:ip地址
"""
import requests
from lxml import etree
from requests.exceptions import RequestException


def get_html(url):
    # headers = {
    #     'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 55.0.2883.87Safari / 537.36'
    # }
    try:
        html = requests.get(url)
        if html.status_code == 200:
            html.encoding = "gbk"
            return html.text
        return None
    except RequestException:
        return None

def get_city_name(url):
    html = get_html(url)
    xpath_etree = etree.HTML(html)
    city_name = xpath_etree.xpath('//ul[@class="ul1"]/li[2]/text()')[0]
    city_name = city_name.split("：")[1]
    city_name = city_name.split("  ")[0]

    return city_name


def main(ip_addr):
    if not ip_addr:
        ip_addr = '58.30.0.0'
    url = 'http://www.ip138.com/ips138.asp?ip={}'.format(str(ip_addr))
    city_name = get_city_name(url)
    return city_name[3:]

if __name__ == '__main__':
    main()