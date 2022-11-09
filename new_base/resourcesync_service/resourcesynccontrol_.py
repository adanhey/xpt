import hashlib
import jsonpath
from new_base.resourcesync_service import *
import base64
from hashlib import *


class Control_resourcesync(Resourcesync_service_interface):
    def get_control_result(self, filter=None, page=None, pageSize=None, orderBy=None):
        url = '%s/api/resourcesync/control' % self.host
        data = {
            '$filter': filter,
            '$page': page,
            '$pageSize': pageSize,
            '$orderBy': orderBy,
        }
        result = self.get_request(url=url, param=data)
        return result

    def distribute_control(self, sendType, readType=1, cacheType=None, *args):
        url = '%s/api/resourcesync/control' % self.host
        data = {
            "sendData": args,
            # {
            #     "gatewayIdentifier": "10",
            #     "deviceName": "设备ABC",
            #     "data": [
            #         {
            #             "measurementIdentifier": "111",
            #             "propertyName": "温度",
            #             "sendContent": "2"
            #         }
            #     ]
            # },
            "cacheType": cacheType,
            "sendType": sendType,
            "readType": readType
        }
        result = self.post_request(url=url, json=data)
        return result

    def update_control_result(self, idcc, timestamp, readRsp=None, *args):
        url = '%s/api/resourcesync/control/%s' % (self.host, idcc)
        data = {
            "id": idcc,
            "timestamp": timestamp,
            "readRsp": readRsp,
            "writeRsp": args
        }
        result = self.patch_request(url=url, json=data)
        return result


b = Control_resourcesync()
# 查询控制量下发记录
# print(b.get_control_result().text)
senddata = {
    "gatewayIdentifier": "10085",
    "deviceName": "设备ABC",
    "data": [{
        "measurementIdentifier": "111",
        "propertyName": "温度",
        "sendContent": "2"
    }]
}
# 控制量下发
print(b.distribute_control(2, 1, 1, senddata).text)
# 控制量下发结果更新
# print(b.update_control_result("123", 123456541532).text)
