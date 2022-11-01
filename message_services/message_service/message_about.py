from message_services.message_service import *


class Message_ability(Message_service_interface):
    def message_ext(self, serviceName, timeFieldValue=None):
        url = '%s/api/message/data/ext' % self.host
        data = {
            'serviceName': serviceName,
            'timeFieldValue': timeFieldValue
        }
        result = self.post_request(url=url, json=data)
        return result

    def message_notice(self, filter=None, filter1=None, page=None, pageSize=None, orderBy=None, pagination=None):
        url = '%s/api/message/notices' % self.host
        data = {
            '$filter': filter,
            '$filter1': filter1,
            '$page': page,
            '$pageSize': pageSize,
            '$orderBy': orderBy,
            'pagination': pagination
        }
        result = self.get_request(url=url, param=data)
        return result.message_ext

    def message_data(self, service_name, filter=None, page=None, pageSize=None, orderBy=None):
        url = '%s/api/message/data/%s' % (self.host, service_name)
        data = {
            '$filter': filter,
            '$page': page,
            '$pageSize': pageSize,
            '$orderBy': orderBy
        }
        result = self.get_request(url=url, param=data)
        return result

    def message_confirm(self,msg_id,msgStatus=0):
        url = '%s/api/message/data/%s/confirm'%(self.host,msg_id)
        data= {
            'id': msg_id,
            'msgStatus': msgStatus
        }
        result = self.post_request(url=url, json=data)
        return result


b = Message_ability()
# print(b.message_notice().text)
print(b.message_confirm('alarm').text)
