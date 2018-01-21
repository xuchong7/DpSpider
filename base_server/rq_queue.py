# coding: utf-8

from redis import Redis
from rq import Queue

conn = Redis(host='localhost', port=6379, db=1, password='tmac92321')

request_q = Queue('request', connection=conn)
process_q = Queue('process', connection=conn)
mail_q = Queue('mail', connection=conn)