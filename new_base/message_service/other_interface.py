from new_base.message_service import *


class Message_other(Message_service_interface):
    def db_connect_test(self, dbType, jdbcUrl, dbUserName, dbPwd):
        '''
        输入的db类型的数据较多，可能会输入错误，所以调用该接口，可进行输入db数据源的检测，来判断是否能正常连通。
        能正常连通会返回data数据，否则不会返回。
        :param dbType:数据库类型名称(MySQL、Oracle等关系型数据库)，目前已支持MySQL。
        :param jdbcUrl:	db消息类型对应的数据库连接字符串(需要进行base64编码，解码后最大长度为255个字符)
        :param dbUserName:db消息类型对应的数据库用户名称 (最大长度为 100 个字符)
        :param dbPwd:	db消息类型对应的数据库用户密码 (最大长度为 100 个字符)
        '''
        url = '%s/api/message/services/datasourcesTest' % self.host
        data = {
            'dbType': dbType,
            'jdbcUrl': jdbcUrl,
            'dbUserName': dbUserName,
            'dbPwd': dbPwd
        }
        result = self.post_request(url=url, json=data)
        return result

    def http_listen(self, httpIdentify, msgType, msgTime, msgId, msgData, accountIds=None):
        '''

        :param httpIdentify:http标识
        :param accountIds:账号，多个逗号隔开，不传则默认值为-1。
        :param msgType:消息数据类型(1-text、2-link、3-actionCard)
        :param msgTime:消息时间(时间字符串)
        :param msgId:消息id(用来处理是新增还是修改，只支持修改msgData)
        :param msgData:消息内容(格式详见示例)
        :return:
        '''
        url = '%s/api/message/services/monitor' % self.host
        data = {
            'httpIdentify': httpIdentify,
            'accountIds': accountIds,
            'msgType': msgType,
            'msgTime': msgTime,
            'msgId': msgId,
            'msgData': msgData
        }
        result = self.post_request(url=url, json=data)
        return result

    def robots_batchquery(self, *args):
        url = '%s/api/message/robots/batchQuery' % self.host
        data = {
            'method': 'queryBind',
            'data': []
        }
        for i in args:
            data['data'].append(i)
        result = self.post_request(url=url,json=data)
        return result

    def robot_bind(self,robotId,account=None):
        url = '%s/api/message/robot-bind'%self.host
        data = {
            'robotId': robotId,
            'account': account
        }
        result = self.post_request(url=url,json=data)
        return result

    def robot_debind(self,robotId,account=None):
        url = '%s/api/message/robot-bind/delete'%self.host
        data = {
            'robotId': robotId,
            'account': account
        }
        result = self.post_request(url=url,json=data)
        return result

# b = Message_other()
# print(b.db_connect_test('Mysql', 'amRiYzpteXNxbDovL215c3FsLmJhc2UuaGM6NTYwNi9kYl9wbGF0X3J1bGVfZW5naW5lP3VzZVVuaWNvZGU9dHJ1ZS'
#                            'ZjaGFyYWN0ZXJFbmNvZGluZz11dGYtOA==', 'root', 'Server@2014Server').text)
# print(b.http_listen("123","1","2021-07-01 00:00:00","10086",{"content": "消息1"},"a,b").text)
# print(b.robots_batchquery('6360e30ebf578c6b0ac41a0a').text)
# print(b.robot_debind('6360e30ebf578c6b0ac41a0a').text)