import os

DIR_PATH = os.path.abspath(os.path.dirname(__file__))

MAIL_SERVER = 'smtpserver'
MAIL_SENDER = 'name@email.com'
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'
TO_MAIL_LIST = [
    'name@email.com',
]

CITY_DICT = {
    'shenzhen': u'深圳',
    'guangzhou': u'广州',
    }

EVENT_START_URL = 'http://s.dianping.com/event/{0}'
DEAL_START_URL = 'http://t.dianping.com/list/{0}/items_40s9153?desc=1&sort=new'

EVENT_HEADERS = {
    'Host': 's.dianping.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'application/json, text/javascript',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Request': 'JSON',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8;',
    'Referer': 'http://s.dianping.com/event/{0}',
    'Content-Length': '137',
    'Cookie': 'aburl=1; cy=7; cye={0}; _hc.v="\"fbaecc80-3665-4742-9f7d-d5ee535e7c43.1495034231\""; JSESSIONID=97EDAB5C6F5BB181700C92BE7F77C7B8; isChecked=checked',
    'Connection': 'keep-alive',
}
