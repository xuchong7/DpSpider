import requests

from dp_logger import logger
from base_server.dp_processor import DpProcessor
from base_server.rq_queue import request_q
from base_server.rq_job import request_data_job


class DpBaseSpider:
    def __init__(self, city, start_url):
        self.city = city
        self.start_url = start_url.format(self.city)

    def start(self, server):
        logger.info('Start DpBasepider')
        request_q.enqueue(request_data_job, server, self)

    def request_data(self, url, headers=None, data=None, method='GET'):
        logger.info('Request Data')
        logger.info(url)
        try:
            if method == 'GET':
                response = requests.get(url)
            else:
                response = requests.post(url, headers=headers, data=data)
        except Exception as e:
            return None, str(e)
        if response.status_code != 200:
            error_info = u'哎呀请求{0}失败了！code: {1}'.format(url, response.status_code)
            logger.info(error_info)
            return None, error_info
        logger.info('Response get!')
        return response, None
