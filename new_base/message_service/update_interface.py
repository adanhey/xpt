import base64
from new_base.message_service import *
from list_interface import *


class Message_update(Message_service_interface):
    def message_service_update(self, service_id, name, serviceType=None, msgType=None, httpMonitor=None,
                               httpIdentify=None, httpUrl=None, description=None, dbType=None, jdbcUrl=None,
                               dbUserName=None, dbPwd=None, dbSql=None, status=None, timeField=None,
                               timeFieldDefault=None):
        '''
        修改消息服务基本信息。字段约束同新增
        :param name:消息服务名称
        :param serviceType:消息服务类型(1-http、2-db)
        :param msgType:消息数据类型(1-text、2-link、3-actionCard)
        :param httpMonitor:http监听 0:未监听，定时任务获取数据 1:主动监听，由其他服务调用(不传则默认值0)
        :param httpIdentify:http标识，使用http监听时唯一标识符(区分大小写)，如果是http主动监听，则必传(最大长度为 50个字符)，
            结合http监听接口进行使用。
        :param httpUrl:消息服务http-url，当serviceType类http时，该字段必填。(需要进行base64编码，解码后最大长度为255个字符)
        :param description:消息服务描述
        :param dbType:数据库类型名称(MySQL、Oracle等关系型数据库)，目前已支持MySQL。当serviceType为db时，该字段必填。
        :param jdbcUrl:db消息类型对应的数据库连接字符串 ，当serviceType类db时，该字段必填。(需要进行base64编码，解码后最大长度为255个字符)
        :param dbUserName:db消息类型对应的数据库用户名称 ，当serviceType类db时，该字段必填。
        :param dbPwd:db消息类型对应的数据库用户密码
        :param dbSql:db消息类型对应的数据库查询SQL(SQL中可使用:绑定变量) ，当serviceType类db时，该字段必填。
            (需要进行base64编码，解码后最大长度为1024个字符)
        :param status:使用状态（1：正常 0：停用）
        :param timeField:时序属性
        :param timeFieldDefaul:时序属性默认值
        :return:
        '''
        url = '%s/api/message/services/%s' % (self.host, service_id)
        data = {
            'name': name,
            'serviceType': serviceType,
            'msgType': msgType,
            'httpMonitor': httpMonitor,
            'httpIdentify': httpIdentify,
            'httpUrl': httpUrl,
            'description': description,
            'dbType': dbType,
            'jdbcUrl': jdbcUrl,
            'dbUserName': dbUserName,
            'dbPwd': dbPwd,
            'dbSql': dbSql,
            'status': status,
            'timeField': timeField,
            'timeFieldDefault': timeFieldDefault
        }
        result = self.patch_request(url=url, json=data)
        return result

    def robots_update(self, robot_name, name, service, params, description=None):
        service = base64.b64encode(bytes(service, encoding='UTF-8'))
        obje = Message_list()
        res = obje.robots_list(pageSize=1000).json()
        robot_id = "1"
        for i in res['data']['result']:
            if i['name'] == robot_name:
                robot_id = i['id']
        url = '%s/api/message/robots/%s' % (self.host,robot_id)
        data = {
            'id': robot_id,
            'name': name,
            'service': str(service)[2:-1],
            'params': params,
            'description': description
        }
        result = self.patch_request(url=url, json=data)
        return result


b = Message_update()
# print(b.message_service_update('6360cf30bf578c6b0ac419fc', 'cccc22', status=0).text)
# print(b.robots_update('dfff22', 'dfhffh', 'http://132', 'sdfhjl;').text)
