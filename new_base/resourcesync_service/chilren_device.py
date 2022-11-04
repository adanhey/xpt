import hashlib

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
# print(b.get_subdevices().text)
# 网关子设备新增
# print(b.create_subdevice("541d5","122355","10084").text)
# 网关子设备更新
# cc = {
#             "identifier": "12235",
#             "status": 2,
#             "timestamp": 1625121523000
#         }
# print(b.update_subdevice(cc).text)
# 获取子设备上下线列表
print(b.get_sub_device_onlinelist().text)
