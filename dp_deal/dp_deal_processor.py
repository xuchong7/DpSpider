from base_server.dp_processor import DpProcessor
from setting import DIR_PATH

class DpDealProcessor(DpProcessor):
    def __init__(self):
        self.file_name = '/'.join([DIR_PATH, 'data', 'dp_deal'])
        super(DpDealProcessor, self).__init__()

    def filter_data_list(self, data_list):
        data_list = [data for data in data_list if float(data['now_price']) <= 100 and float(data['now_price']) <= float(data['origin_price']) * 0.4]
        return data_list
