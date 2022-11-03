from new_base.message_service import *

class Message_delete(Message_service_interface):
    def message_service_delete(self,*args):
        url = '%s/api/message/services/batch'%self.host
        data={
            'method':'delete',
            'data': []
        }
        for i in args:
            data['data'].append(i)
        result = self.post_request(url=url,json=data)
        return result

    def robot_delete(self,*args):
        url = '%s/api/message/robots/batch'%self.host
        data={
            'method':'delete',
            'data': []
        }
        for i in args:
            data['data'].append(i)
        result = self.post_request(url=url,json=data)
        return result

b = Message_delete()
# print(b.message_service_delete('6360cf30bf578c6b0ac419fc').text)
print(b.robot_delete('6360e364bf578c6b0ac41a0b').text)