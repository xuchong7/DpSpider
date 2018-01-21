# -*- coding: utf-8 -*-

import logging
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from setting import MAIL_SERVER, MAIL_SENDER, MAIL_USERNAME, MAIL_PASSWORD

from dp_logger import logger

class Mail:
    def __init__(self, receiver_list):
        self.sender = MAIL_SENDER
        self.smtpserver = MAIL_SERVER
        self.username = MAIL_USERNAME
        self.password = MAIL_PASSWORD
        self.receiver_list = receiver_list

    # def send_mail(self, subject, receiver_list, data_list):
    #     logger.info('Start send email')
    #     mail_msg = self.init_mail_msg(data_list)
    #     msg = MIMEText(mail_msg, 'html', 'utf-8')
    #     msg['Subject'] = self.subject
    #     smtp = smtplib.SMTP()
    #     smtp.connect(self.smtpserver)
    #     smtp.login(self.username, self.password)
    #     smtp.sendmail(self.sender, receiver_list, msg.as_string())
    #     logger.info('Send email ok')
    #     smtp.quit()

    def send_mail(self, data_list, city_name):
        logger.info('Start send email')
        mail_msg = self.init_mail_msg(data_list)
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['Subject'] = city_name + self.subject
        smtp = smtplib.SMTP()
        smtp.connect(self.smtpserver)
        smtp.login(self.username, self.password)
        smtp.sendmail(self.sender, self.receiver_list, msg.as_string())
        logger.info('Send email ok')
        smtp.quit()
    
