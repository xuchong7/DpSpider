# -*- coding: utf-8 -*-

import logging
from dp_logger import logger
from base_server.mail import Mail


class EventMail(Mail):
    def __init__(self, receiver_list):
        self.subject = '新霸王餐提醒'
        super(EventMail, self).__init__(receiver_list)

    def init_mail_msg(self, event_list):
        table_html = u'''
        <html>
        <head>
        <link href="https://cdn.bootcss.com/bootstrap/4.0.0-alpha.6/css/bootstrap-grid.css" rel="stylesheet">
        </head>
        <body>
            <table class="table table-striped table-hover">
                <thead>
                    <tr>
                        <th>标题</th>
                        <th>passcard</th>
                        <th>体验券</th>
                    </tr>
                </thead>
                <tbody>
                    {event_list_html}
                </tbody>
            </table>
        </body>
        </html>
        '''
        event_html = u'''
            <tr>
                <td><a href="{full_url}">{name}</a></td>
                <td>{is_passcard}</td>
                <td>{is_try}</td>
            </tr>
        '''
        event_list_html = u''
        for event in event_list:
            full_url = u'http://s.dianping.com' + event['url']
            event_list_html += event_html.format(full_url=full_url, name=event['name'], is_try=event['is_try'],is_passcard=event['is_passcard'])
        html = table_html.format(event_list_html=event_list_html)
        return html
