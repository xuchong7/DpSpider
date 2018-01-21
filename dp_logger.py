# -*- coding: utf-8 -*-

import logging
from setting import DIR_PATH

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-5s %(asctime)s %(levelname)-5s %(message)s', '%a, %d %b %Y %H:%M:%S',)
stream_handle = logging.StreamHandler()
stream_handle.setFormatter(formatter)
logger.addHandler(stream_handle)
file_handle = logging.FileHandler('/'.join([DIR_PATH, 'data', 'dp_spider.log']))
file_handle.setFormatter(formatter)
logger.addHandler(file_handle)
