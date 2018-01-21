# coding: utf-8

from dp_logger import logger
from base_server.rq_queue import process_q, mail_q

def request_data_job(server, spider):
    logger.info('In rq job request_data')
    data_list, error_info = spider.get_data()
    if error_info:
        logger.error(error_info)
    logger.info('data_list:{0}'.format(data_list))
    process_q.enqueue(process_data_job, server, spider, data_list)


def process_data_job(server, spider, data_list):
    logger.info('In rq job process_data')
    logger.info('data_list:{0}'.format(data_list))
    new_data_list = server.processor.process_data_list_with_file(data_list, spider.city)
    if  new_data_list:
        logger.info()
        mail_q.enqueue(mail_job, server, spider, new_data_list)


def mail_job(server, spider, new_data_list):
    logger.info('In rq job process_data')
    server.mail.send_mail(new_data_list, spider.city)