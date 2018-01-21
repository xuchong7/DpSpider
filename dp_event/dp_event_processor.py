from base_server.dp_processor import DpProcessor
from setting import DIR_PATH


class DpEventProcessor(DpProcessor):
    def __init__(self):
        self.file_name = '/'.join([DIR_PATH, 'data', 'dp_event'])
        super(DpEventProcessor, self).__init__()

    def filter_data_list(self, data_list):
        return data_list
