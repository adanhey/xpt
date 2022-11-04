import hashlib

from new_base.resourcesync_service import *
import base64
from hashlib import *


class Device_config(Resourcesync_service_interface):
    def get_distribution_result(self, filter=None, pagination=0, page=None, pageSize=None, orderBy=None):
        url = '%s/api/resourcesync/config' % self.host
        data = {
            '$filter': filter,
            '$page': page,
            '$pageSize': pageSize,
            '$orderBy': orderBy,
            'pagination': pagination
        }
        result = self.get_request(url=url, param=data)
        return result

    def distribution_config(self, gatewayDeviceIdentifier, syncId, headerList=None, recycleList=None,
                            collectModelIdentifier=None, collectModelVersion=None, fileId=None):
        url = '%s/api/resourcesync/config' % self.host
        data = {
            "collectModelIdentifier": collectModelIdentifier,
            "collectModelVersion": collectModelVersion,
            "gatewayDeviceIdentifier": gatewayDeviceIdentifier,
            "syncId": syncId,
            "fileId": fileId,
            "headerList": headerList,
            "recycleList": recycleList
        }
        result = self.post_request(url=url, json=data)
        return result

    def update_config_reuslt(self, errorCode, result, idcc, progress, timestamp, desc=None):
        url = '%s/api/resourcesync/config/%s' % (self.host, idcc)
        data = {
            "id": idcc,
            "progress": progress,
            "errorCode": errorCode,
            "desc": desc,
            "timestamp": timestamp,
            "result": result,
        }
        result = self.patch_request(url=url, json=data)
        return result

    def config_send_module(self,collectModelIdentifier,gatewayDeviceIdentifier):
        url = '%s/api/resourcesync/config/sendModule' % self.host
        data = {
            "collectModelIdentifier": collectModelIdentifier,
            "gatewayDeviceIdentifier": gatewayDeviceIdentifier,
            "configList": [{
                "configType": "deviceConfigcfg",
                "contentDataType": "2",
                "versionNum": "aaa123456",
                "configContent": [{
                    "identifier": "zx123",
                    "phyPort": "1",
                    "protocol": "1111",
                    "address": "192.168.1.100",
                    "port": 20
                }]
            }]
        }


b = Device_config()
# 网关配置下发记录查询
# print(b.get_distribution_result().text)
# 网关配置下发
# print(b.distribution_config("1", "2").text)
# 网关配置下发结果更新
# bddd = [{
#     "module": "eventsvr",
#     "deviceIdentifier": "aaa",
#     "status": 1,
#     "desc": "edge update config ok!"
#   }]
# print(b.update_config_reuslt("812400005255",bddd,"123","100",1625121523000).text)
