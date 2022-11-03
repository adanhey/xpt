from new_base.message_service import *


class Message_list(Message_service_interface):
    def message_service_list(self, filter=None, page=None, pageSize=None, orderBy=None):
        '''
        分页查询消息服务列表
        :param filter:查询过滤条件，详见 $filter 使用说明（多个字段使用英文逗号连接）
        :param page:分页操作页码，默认值为 1
        :param pageSize:每页返回记录数，默认值为 10
        :param orderBy:排序，asc 表示升序，desc 表示降序，默认为升序排列；传参格式：属性1 desc,属性2 asc
        '''
        url = '%s/api/message/services' % self.host
        data = {
            '$filter': filter,
            '$page': page,
            '$pageSize': pageSize,
            '$orderBy': orderBy
        }
        result = self.get_request(url=url, param=data)
        return result

    def robots_list(self, filter=None, page=None, pageSize=None, orderBy=None, bindType=None, account=None):
        '''
        获取消息机器人列表数据
        :param filter:查询过滤条件，详见 $filter 使用说明
        :param page:分页操作页码，默认值为 1
        :param pageSize:每页返回记录数，默认值为 10
        :param orderBy:排序，asc 表示升序，desc 表示降序，默认为升序排列；传参格式：属性1 desc,属性2 asc
        :param bindType:绑定类型(1： 绑定 0：未绑定)
        :param account:登录账号(用于查询绑定/未绑定该账号的机器人)，不传则会取token对应的账号，如果bindType为空，则忽略账号信息。
        '''
        url = '%s/api/message/robots' % self.host
        data = {
            'filter': filter,
            'page': page,
            'pageSize': pageSize,
            'orderBy': orderBy,
            'bindType': bindType,
            'account': account
        }
        result = self.get_request(url=url,param=data)
        return result

c = Message_list()
# print(c.message_service_list().text)
# print(c.robots_list().text)
