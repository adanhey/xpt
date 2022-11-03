import datetime
import threading
import time
import logging
from list_interface import *
from other_interface import *
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename='wrong.log', encoding='UTF-8')
logger.addHandler(file_handler)


def message_lists():
    b = Message_list()
    nowtime = time.time()
    for i in range(100):
        result = b.message_service_list()
        print('%s:  %s   ' % (nowtime, result.status_code))
        print(result.text)
        if result.status_code != 200:
            logger.info('%s: %s' % (str(nowtime), result.text))
        logger.removeHandler(file_handler)
b = Message_other()
def run_lots():
    nowtime = time.time()
    for i in range(1000):
        msgid = '%s_%s'%(str(nowtime),i)
        print(b.http_listen("alarm","1","2021-02-03 00:00:00",msgid,{"content": "消息1"},"admin").text)

thread1 = threading.Thread(name='t1', target=run_lots(), args=())
thread2 = threading.Thread(name='t2', target=run_lots(), args=())
thread3 = threading.Thread(name='t3', target=run_lots(), args=())
thread4 = threading.Thread(name='t4', target=run_lots(), args=())
thread5 = threading.Thread(name='t5', target=run_lots(), args=())
thread1.start()  # 启动线程1
thread2.start()  # 启动线程2
thread3.start()  # 启动线程3
thread4.start()  # 启动线程4
thread5.start()  # 启动线程5
