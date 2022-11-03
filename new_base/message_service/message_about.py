import threading
import time

from new_base.message_service import *


class Message_ability(Message_service_interface):
    def message_ext(self, serviceName, timeFieldValue=None):
        url = '%s/api/message/data/ext' % self.host
        data = {
            'serviceName': serviceName,
            'timeFieldValue': timeFieldValue
        }
        result = self.post_request(url=url, json=data)
        return result

    def message_notice(self, filter=None, filter1=None, page=None, pageSize=None, orderBy=None, pagination=None):
        url = '%s/api/message/notices' % self.host
        data = {
            '$filter': filter,
            '$filter1': filter1,
            '$page': page,
            '$pageSize': pageSize,
            '$orderBy': orderBy,
            'pagination': pagination
        }
        result = self.get_request(url=url, param=data)
        return result.message_ext

    def message_data(self, service_name, pagination=None, criticalId=None, filter=None, startTime=None, endTime=None,
                     offset=None, page=None, pageSize=None, orderBy=None):
        url = '%s/api/message/data/%s' % (self.host, service_name)
        data = {
            '$filter': filter,
            '$page': page,
            '$pageSize': pageSize,
            '$orderBy': orderBy,
            'pagination': pagination,
            'criticalId': criticalId,
            'offset': offset,
            'startTime': startTime,
            'endTime': endTime
        }
        result = self.get_request(url=url, param=data)
        return result

    def message_confirm(self, msg_id, msgStatus=0):
        url = '%s/api/message/data/%s/confirm' % (self.host, msg_id)
        data = {
            'id': msg_id,
            'msgStatus': msgStatus
        }
        result = self.post_request(url=url, json=data)
        return result
b = Message_ability()
def cc():
    print(time.time())
    # print(b.message_notice().text)
    print(time.time(),
        b.message_data('alarm',pagination=2, startTime='2022-06-02 00:00:00', offset=None, criticalId=None, page=None, pageSize=100,
                       endTime='2022-11-03 00:00:00', filter=None, orderBy=None).text)
thread1 = threading.Thread(name='t1', target=cc(), args=())
thread2 = threading.Thread(name='t2', target=cc(), args=())
thread3 = threading.Thread(name='t3', target=cc(), args=())
thread4 = threading.Thread(name='t4', target=cc(), args=())
thread5 = threading.Thread(name='t5', target=cc(), args=())
thread1.start()  # 启动线程1
thread2.start()  # 启动线程2
thread3.start()  # 启动线程3
thread4.start()  # 启动线程4
thread5.start()  # 启动线程5


