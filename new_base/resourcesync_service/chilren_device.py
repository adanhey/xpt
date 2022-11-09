import hashlib
import threading
import time

from new_base.resourcesync_service import *
import base64
from hashlib import *


class Resource_children(Resourcesync_service_interface):
    def get_subdevices(self, filter=None, pagination=0, page=None, pageSize=None, orderBy=None):
        url = '%s/api/resourcesync/subDevices' % self.host
        data = {
            '$filter': filter,
            '$page': page,
            '$pageSize': pageSize,
            '$orderBy': orderBy,
            'pagination': pagination
        }
        result = self.get_request(url=url, param=data)
        return result

    def create_subdevice(self, name, identifier, gatewayIdentifier, factoryBrandName=None, subModelName=None,
                         collectProtocolName=None,
                         portType=None, address=None, accessPort=None, port=None):
        url = '%s/api/resourcesync/subDevices' % self.host
        data = {
            "name": name,
            "identifier": identifier,
            "factoryBrandName": factoryBrandName,
            "gatewayIdentifier": gatewayIdentifier,
            "subModelName": subModelName,
            "collectProtocolName": collectProtocolName,
            "portType": portType,
            "address": address,
            "port": port,
            "accessPort": accessPort
        }
        result = self.post_request(url=url, json=data)
        return result

    def update_subdevice(self, *args):
        url = '%s/api/resourcesync/subDevices/batch' % (self.host)
        data = {
            "list": args
        }
        result = self.post_request(url=url, json=data)
        return result

    def get_sub_device_onlinelist(self, filter=None, page=None, pagesize=None, orderBy=None, startTime=None,
                                  endTime=None, pagination=None, criticalId=None, offset=None):
        url = '%s/api/resourcesync/subDevices/getOnlineList' % (self.host)
        data = {
            "$filter": filter,
            "$page": page,
            "$pageSize": pagesize,
            "$orderBy": orderBy,
            "startTime": startTime,
            "endTime": endTime,
            "pagination": pagination,
            "criticalId": criticalId,
            "offset": offset
        }
        result = self.get_request(url=url, param=data)
        return result


b = Resource_children()


# 获取网关子设备列表
# print(b.get_subdevices(filter='1243rtgnb refgbn23r').text)
# 网关子设备新增
# print(b.create_subdevice("acv224acv224acv224acv224acv224acv224acv224","51122354623","10084").text)
# 网关子设备更新
def run_ds(useless):
    nowtime = time.time()
    nowtime = int(nowtime * 1000)
    print(nowtime)
    cc = [{
        "identifier": "12235",
        "status": 2,
        "timestamp": nowtime
    }]
    vv = {
        "identifier": "12235",
        "status": 1,
        "timestamp": nowtime
    }
    # for i in range(1000):
    print(b.update_subdevice(cc).text)
    # 获取子设备上下线列表
#     print(b.get_sub_device_onlinelist(page=1, pagesize=500, pagination=2, orderBy='id asc',
#                                       criticalId='1589858150692220930'
# ).text)


thread1 = threading.Thread(name='t1', target=run_ds(2), args=())
# thread2 = threading.Thread(name='t2', target=run_ds(1), args=())
# thread3 = threading.Thread(name='t3', target=run_ds(3), args=())
# thread4 = threading.Thread(name='t4', target=run_ds(5), args=())
# thread5 = threading.Thread(name='t5', target=run_ds(4), args=())
thread1.start()  # 启动线程1
# thread2.start()  # 启动线程2
# thread3.start()  # 启动线程3
# thread4.start()  # 启动线程4
# thread5.start()  # 启动线程5
