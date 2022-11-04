import hashlib

from new_base.resourcesync_service import *
import base64
from hashlib import *


class Resource_create(Resourcesync_service_interface):
    def get_device(self, filter=None, pagination=0, page=None, pageSize=None, orderBy=None):
        url = '%s/api/resourcesync/gatewayDevices' % self.host
        data = {
            '$filter': filter,
            '$page': page,
            '$pageSize': pageSize,
            '$orderBy': orderBy,
            'pagination': pagination
        }
        result = self.get_request(url=url, param=data)
        return result

    def create_device(self, name, identifier, gatewayModel, instanceId, businessType=None, tenantId=None,
                      tenantName=None, registerSim=None, orgPathName=None, orgId=None):
        url = '%s/api/resourcesync/gatewayDevices' % self.host
        data = {
            "name": name,
            "identifier": identifier,
            "gatewayModel": gatewayModel,
            "instanceId": instanceId,
            "businessType": businessType,
            "tenantId": tenantId,
            "tenantName": tenantName,
            "registerSim": registerSim,
            "orgId": orgId,
            "orgPathName": orgPathName
        }
        result = self.post_request(url=url, json=data)
        return result

    def update_device(self, identifier, name=None, gatewayModel=None, instanceId=None, sim=None, businessType=None,
                      tenantId=None, tenantName=None, registerSim=None, orgPathName=None, orgId=None, onlineParams=None,
                      cdParams=None, softParams=None, configParams=None, eventLog=None):
        url = '%s/api/resourcesync/gatewayDevices/%s' % (self.host, identifier)
        data = {
            "name": name,
            "identifier": identifier,
            "gatewayModel": gatewayModel,
            "instanceId": instanceId,
            "businessType": businessType,
            "tenantId": tenantId,
            "tenantName": tenantName,
            "registerSim": registerSim,
            "orgId": orgId,
            "orgPathName": orgPathName,
            "sim": sim,
            "onlineParams": onlineParams,
            "cdParams": cdParams,
            "softParams": softParams,
            "configParams": configParams,
            "eventLog": eventLog
        }
        result = self.patch_request(url=url, json=data)
        return result

    def device_detail(self, identifier):
        url = '%s/api/resourcesync/gatewayDevices/%s' % (self.host, identifier)
        result = self.get_request(url=url)
        return result

    def make_accessToken(self, identifier, salt, secret, type="sha"):
        accessToken = ''
        if type == "sha":
            accessToken = sha256(('%s%s' % (identifier, salt)).encode("utf-8")).hexdigest() + sha256(
                ('%s%s' % (secret, salt)).encode("utf-8")).hexdigest()
        elif type == "md5":
            accessToken = hashlib.md5(('%s%s' % (identifier, salt)).encode("utf-8")).hexdigest() + hashlib.md5(
                ('%s%s' % (secret, salt)).encode("utf-8")).hexdigest()
        return accessToken

    def device_register(self, identifier, type, salt=None, encryptionType=None, secret=None):
        url = '%s/api/resourcesync/gatewayDevices/%s/register' % (self.host, identifier)
        accessToken = None
        if secret:
            accessToken = self.make_accessToken(identifier, salt, secret)
        data = {
            "identifier": identifier,
            "type": type,
            "salt": salt,
            "encryptionType": encryptionType,
            "accessToken": accessToken
        }
        result = self.post_request(url=url, json=data)
        return result

    def get_onlinelist(self, identifier, filter=None, page=None, pagesize=None, orderBy=None, startTime=None,
                       endTime=None, pagination=None, criticalId=None, offset=None):
        url = '%s/api/resourcesync/gatewayDevices/%s/getOnlineList' % (self.host, identifier)
        data = {
            "$filter": filter,
            "$page": page,
            "$pageSize": pagesize,
            "$orderBy": orderBy,
            "identifier": identifier,
            "startTime": startTime,
            "endTime": endTime,
            "pagination": pagination,
            "criticalId": criticalId,
            "offset": offset
        }
        result = self.get_request(url=url, param=data)
        return result

    def get_params(self, identifier, filter=None, page=None, pagesize=None, orderBy=None, startTime=None,
                   endTime=None, pagination=None, criticalId=None, offset=None, queryType=None, timeQuery=None):
        url = '%s/api/resourcesync/gatewayDevices/%s/getOnlineList' % (self.host, identifier)
        data = {
            "$filter": filter,
            "$page": page,
            "$pageSize": pagesize,
            "$orderBy": orderBy,
            "identifier": identifier,
            "queryType": queryType,
            "startTime": startTime,
            "endTime": endTime,
            "timeQuery": timeQuery,
            "pagination": pagination,
            "criticalId": criticalId,
            "offset": offset
        }
        result = self.get_request(url=url, param=data)
        return result


b = Resource_create()
# 获取网管设备列表
# print(b.get_device().text)
# 网管设备新增
# print(b.create_device("whatever", "10086", "430DE", 1123214214).text)
# 网关设备更新
# print(b.update_device(10084,"ccvvv").text)
# 网关设备详情
# print(b.device_detail("10084").text)
# 编写accesstoken
# print(str(b.make_accessToken("1234104104101520210", "456", "789","md5")))
# 网关设备注册
# print(b.device_register("10084", 1, 'kfggg', 1, 'uZCOkumZjR').text)
# 获取网关上下线列表
# print(b.get_onlinelist("10084").text)
# 获取网关参数等信息
# print(b.get_params("10084").text)
