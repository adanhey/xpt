import datetime
import threading
import time
import logging
from list_interface import *

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


thread1 = threading.Thread(name='t1', target=message_lists, args=())
thread2 = threading.Thread(name='t2', target=message_lists, args=())
thread3 = threading.Thread(name='t3', target=message_lists, args=())
thread4 = threading.Thread(name='t4', target=message_lists, args=())
thread5 = threading.Thread(name='t5', target=message_lists, args=())
thread1.start()  # 启动线程1
thread2.start()  # 启动线程2
thread3.start()  # 启动线程3
thread4.start()  # 启动线程4
thread5.start()  # 启动线程5
