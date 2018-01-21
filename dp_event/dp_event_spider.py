# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

from base_server.server import Server
from base_server.dp_base_spider import DpBaseSpider
from dp_event.dp_event_processor import DpEventProcessor
from dp_logger import logger
from dp_event.event_mail import EventMail
from setting import EVENT_HEADERS as HEADERS
from setting import CITY_DICT, EVENT_START_URL, TO_MAIL_LIST


class DpEventSpider(DpBaseSpider):
    def __init__(self, city, start_url):
        super(DpEventSpider, self).__init__(city, start_url)

    def get_data(self):
        response, error_info = self.request_data(self.start_url)
        html = response.content
        if error_info:
            return None, error_info
        event_info_list = []
        event_info_list.extend(self.get_event(html))
        activity_ids, top_event_info_list = self.get_activity_ids_and_top_event_list(html)
        event_info_list.extend(top_event_info_list)
        # for page_no in xrange(2, 7):
        #     logger.info('Start scrap page {0}'.format(page_no))
        #     event_info_list.extend(self.get_more_event(page_no, activity_ids))
        return event_info_list, None

    ##############################
    # 解析html
    ##############################
    def get_activity_ids_and_top_event_list(self, html):
        soup = BeautifulSoup(html, "html5lib")
        top_event_list = soup.find_all('li', class_='monad-recommend')
        top_event_info_list = map(self.get_event_info, top_event_list)
        activity_ids = ','.join(map(lambda x: x['url'].lstrip('/event/'), top_event_info_list))
        return activity_ids, top_event_info_list

    def get_event(self, html):
        soup = BeautifulSoup(html, "html5lib")
        event_list = soup.find_all('ul', class_='monad-default')
        event_info_list = map(self.get_event_info, event_list)
        return event_info_list

    def get_event_info(self, event):
        event_info = {}
        event_info['url'] = event.find('a')['href']
        event_info['name'] = event.find('a')['title']
        event_info['is_try'] = u'体验券' if event.find('span', class_='gift-try J_try_intro') else u'非体验券'
        event_info['is_passcard'] = u'支持passcard' if event.find('span', class_='gift-passcard J_passcard_intro') else u'不支持passcard'
        return event_info

    def get_more_event(self, page, activity_ids):
        headers = copy.deepcopy(HEADERS)
        headers['Referer'] = HEADERS['Referer'].format(self.city)
        headers['Cookie'] = HEADERS['Cookie'].format(self.city)
        payload = {
            'activityIds': activity_ids, # '310931393,1478640245,599385275,1985541007,692753899,781439133',
            'activityStatus': 0,
            'modeId': 0,
            'page': page,
            'passCount': 0,
            'typeId': 0,
        }
        url = 'http://s.dianping.com/ajax/json/activity/offline/moreActivityList'

        response, error_info = self.request_data(url, headers=headers, data=payload, method='POST')
        if error_info:
            logger.info(error_info)
            return None
        try:
            response = response.json()
        except Exception as e:
            error_info = u'解析json失败' + str(e)
            logger.info(error_info)
            return None
        html = response.get('msg', {}).get('html', '')
        return self.get_event(html)


def run():
    spider_list = []
    for city, city_name in CITY_DICT.items():
        spider_list.append(DpEventSpider(city, EVENT_START_URL))
    processor = DpEventProcessor()
    mail = EventMail(TO_MAIL_LIST)
    server = Server(spider_list, processor, mail)
    server.run()
