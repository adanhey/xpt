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

    def distribution_config(self, gatewayDeviceIdentifier, syncId=None, headerList=None, recycleList=None,
                            collectModelIdentifier=None, collectModelVersion=None, fileId=None):
        '''
        给网关设备下发配置
        :param gatewayDeviceIdentifier:网关设备标识
        :param syncId:配置同步id(此次操作的唯一id)
        :param headerList:当文件id不为空时，必填
        :param recycleList:配置标识
        :param collectModelIdentifier:采集模板标识(非回收操作必填)
        :param collectModelVersion:采集模板的版本号(非回收操作必填)
        :param fileId:文件id，有值时直接取文件进行配置下发
        :return:
        '''
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

    def config_send_module(self, collectModelIdentifier, gatewayDeviceIdentifier):
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
        result = self.patch_request(url=url, json=data)
        return result


b = Device_config()
# 网关配置下发记录查询
# print(b.get_distribution_result().text)
# 网关配置下发
header = [
    {
        "cfgIdentifier1": "1",
        "versionNo1": "2",
        "deviceIdentifier": "aaa"
    },
]
print(b.distribution_config("10085", syncId='cvv',
                            collectModelIdentifier='125', collectModelVersion='124').text)
# 网关配置下发结果更新
bddd = [{
    "module": "eventsvr",
    "deviceIdentifier": "aaa",
    "status": 1,
    "desc": "edge update config ok!"
}]
# print(b.update_config_reuslt("12300000000000",bddd,"1589801824482029569","100",1625121523000).text)
# 网关配置增量下发
# print(b.config_send_module("123","10085").text)
