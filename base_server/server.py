# coding: utf-8

from dp_logger import logger
from setting import EVENT_HEADERS as HEADERS
from setting import CITY_DICT, EVENT_START_URL, TO_MAIL_LIST

class Server:
    def __init__(self, spider_list, processor, mail):
        self.spider_list = spider_list
        self.processor = processor
        self.mail = mail

    def run(self):
        for spider in self.spider_list:
            logger.info('{0} start!'.format(spider.city))
            spider.start(self)
