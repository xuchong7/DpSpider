# -*- coding: utf-8 -*-

import logging
from dp_logger import logger
from base_server.mail import Mail


class DealMail(Mail):
    def __init__(self):
        super(DealMail, self).__init__()

    def init_mail_msg(self, deal_list):
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
                        <th>描述</th>
                        <th>价格</th>
                        <th>原价</th>
                    </tr>
                </thead>
                <tbody>
                    {deal_list_html}
                </tbody>
            </table>
        </body>
        </html>
        '''
        deal_html = u'''
            <tr>
                <td><a href="{full_url}">{name}</a></td>
                <td>{description}</td>
                <td>{now_price}</td>
                <td>{origin_price}</td>
            </tr>
        '''
        deal_list_html = u''
        for deal in deal_list:
            full_url = u'http://t.dianping.com' + deal['url']
            deal_list_html += deal_html.format(full_url=full_url,
                                               name=deal['name'],
                                               description=deal['description'],
                                               now_price=deal['now_price'],
                                               origin_price=deal['origin_price'])
        html = table_html.format(deal_list_html=deal_list_html)
        return html
