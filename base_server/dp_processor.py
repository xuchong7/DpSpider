# -*- coding: utf-8 -*-

import logging

from dp_logger import logger


class DpProcessor:
    def __init__(self):
        self.new_data_list = []

    def process_data_list_with_file(self, data_list, city):
        logger.info('Inprocessor')
        data_list = self.filter_data_list(data_list)
        save_file_name = '{0}_{1}'.format(self.file_name, city)
        logger.info(save_file_name)
        with open(save_file_name, 'r') as f:
            file_data = f.read().strip()
        origin_url_list = file_data.split(',')
        for data in data_list:
            if data['url'] not in origin_url_list:
                self.new_data_list.append(data)
        current_url_list = [data['url'] for data in data_list]
        current_url_str = ','.join(current_url_list)
        with open(save_file_name, 'w') as f:
            f.write(current_url_str)
        logger.info('origin_url_list:{0}'.format(origin_url_list))
        logger.info('current_url_list:{0}'.format(current_url_list))
        logger.info('new_data_list:{0}'.format(self.new_data_list))
        return self.new_data_list
