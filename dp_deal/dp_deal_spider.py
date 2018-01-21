# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from base_server.dp_base_spider import DpBaseSpider
from dp_deal.dp_deal_processor import DpDealProcessor
from dp_logger import logger
from dp_deal.deal_mail import DealMail
from setting import CITY_DICT, DEAL_START_URL, TO_MAIL_LIST


class DpDealSpider(DpBaseSpider):
    def __init__(self, city, start_url):
        super(DpDealSpider, self).__init__(city, start_url)

    def get_data(self):
        response, error_info = self.request_data(self.start_url)
        html = response.content
        if error_info:
            return None, error_info
        deal_info_list = []
        deal_info_list.extend(self.get_deal(html))
        return deal_info_list, None

    def get_deal(self, html):
        soup = BeautifulSoup(html, "html5lib")
        deal_list = soup.find_all('li', class_='tg-floor-item')
        deal_info_list = map(self.get_deal_info, deal_list)
        return deal_info_list

    def get_deal_info(self, deal):
        deal_info = {}
        deal_info['url'] = deal.find('a', class_='tg-floor-title')['href']
        deal_info['name'] = deal.find('h3').string
        deal_info['description'] = deal.find('h4').string
        deal_info['now_price'] = deal.find('em').string
        deal_info['origin_price'] = deal.find('del').string
        return deal_info


def run():
    def run():
    spider_list = []
    for city, city_name in CITY_DICT.items():
        spider_list.append(DpDealSpider(city, DEAL_START_URL))
    processor = DpDealProcessor()
    mail = DealMail(TO_MAIL_LIST)
    server = Server(spider_list, processor, mail)
    server.run()
