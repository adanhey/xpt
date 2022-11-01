from message_services.message_service import *
import base64


class Message_create(Message_service_interface):
    def message_service_create(self, name, serviceType, msgType, httpMonitor=None, httpIdentify=None, httpUrl=None,
                               clientId=None, secret=None, tokenUrl=None, description=None, dbType=None, jdbcUrl=None,
                               dbUserName=None, dbPwd=None, dbSql=None, timeField=None, timeFieldDefault=None):
        '''
        添加消息服务，服务名称保持唯一。消息服务为http方式时，当前支持get、post方式。http服务需要鉴权，故需要填写客户端凭证信息，
            (clientId、secret、tokenUrl有一项为空)则会使用默认客户端凭证信息(默认信息在配置文件中)。
        :param name:消息名称(最大长度为 50 个字符，只能包含大小写英文字母、数字、下划线)
        :param serviceType:消息服务类型(1-http、2-db)
        :param msgType:消息数据类型(1-text、2-link、3-actionCard)
        :param httpMonitor:	http监听 0:未监听，定时任务获取数据 1:主动监听，由其他服务调用(不传则默认值0)
        :param httpIdentify:http标识(最大长度为 50 个字符，只能包含大小写英文字母、数字、下划线)，使用http监听时唯一标识符(区分大小写)，
            如果是http主动监听，则必传(最大长度为 50个字符)，结合http监听接口进行使用。
        :param httpUrl:消息服务http-url，当serviceType类型为http时，该字段必填。(由于httpUrl可能会带一些特殊字符，所以需要进行
            base64编码，解码后最大长度为512个字符)
        :param clientId:客户端Id，通过令牌方式获取token，针对于serviceType类型为http使用，不传则默认通用配置项。
        :param secret:加密因子，通过令牌方式获取token，针对于serviceType类型为http使用，不传则默认通用配置项。
        :param tokenUrl:获取token接口地址，通过令牌方式获取token，针对于serviceType类型为http使用，不传则默认通用配置项。
        :param description:消息服务描述(最大长度为 50 个字符，只能包含大小写英文字母、数字、下划线)
        :param dbType:数据库类型名称(MySQL、Oracle等关系型数据库)，目前已支持MySQL。当serviceType为db时，该字段必填。
        :param jdbcUrl:db消息类型对应的数据库连接字符串 ，当serviceType类db时，该字段必填。(需要进行base64编码，解码后最大长度为255个字符)
        :param dbUserName:db消息类型对应的数据库用户名称 ，当serviceType类db时，该字段必填。(最大长度为 100 个字符)
        :param dbPwd:db消息类型对应的数据库用户密码 ，当serviceType类db时，该字段必填。(最大长度为 100 个字符)
        :param dbSql:db消息类型对应的数据库查询SQL(SQL中可使用:绑定变量) ，当serviceType类db时，该字段必填。
            (需要进行base64编码，解码后最大长度为1024个字符)
        :param timeField:时序属性(不填，则默认id)，用于定时任务增量获取数据
        :param timeFieldDefault:时序属性默认值(不填，则默认0)
        '''
        url = '%s/api/message/services' % self.host
        if httpUrl:
            httpUrl = base64.b64encode(bytes(httpUrl))
        data = {
            'name': name,
            'serviceType': serviceType,
            'msgType': msgType,
            'httpMonitor': httpMonitor,
            'httpIdentify': httpIdentify,
            'httpUrl': httpUrl,
            'clientId': clientId,
            'secret': secret,
            'tokenUrl': tokenUrl,
            'description': description,
            'dbType': dbType,
            'jdbcUrl': jdbcUrl,
            'dbUserName': dbUserName,
            'dbPwd': dbPwd,
            'dbSql': dbSql,
            'timeField': timeField,
            'timeFieldDefault': timeFieldDefault
        }
        result = self.post_request(url=url, json=data)
        return result

    def robot_create(self,name,service,params,description):
        '''
        新增消息机器人，机器人名称唯一。服务地址和服务参数的使用方式见4.4.2章节。
        :param name:消息机器人名称(最大长度为 50 个字符，只能包含中文、大小写英文字母、数字、下划线)
        :param service:服务地址(获取消息数据的url)(需要进行base64编码，解码后最大长度为255个字符)
        :param params:服务参数(最大长度为255个字符)
        :param description:消息机器人描述(最大长度为 50 个字符)
        '''
        service = base64.b64encode(bytes(service,encoding='UTF-8'))
        url = '%s/api/message/robots'%self.host
        data= {
            'name': name,
            'service': str(service)[2:-1],
            'params': params,
            'description': description
        }
        result = self.post_request(url=url, json=data)
        return result

c = Message_create()
print(c.robot_create('dfff22','http://www.baidu.com','wqdhifvbe','wqddhjd').text)
