from message_services.message_service import *
from list_interface import *


class Message_detail(Message_service_interface):
    def message_service_detail(self, service_id):
        url = '%s/api/message/services/%s' % (self.host, service_id)
        result = self.get_request(url=url)
        return result

    def robot_detail(self, robot_name):
        obje = Message_list()
        res = obje.robots_list(pageSize=1000).json()
        robot_id = "1"
        for i in res['data']['result']:
            if i['name'] == robot_name:
                robot_id = i['id']
        url = '%s/api/message/robots/%s' % (self.host, robot_id)
        result = self.get_request(url=url)
        return result


b = Message_detail()
# print(b.message_service_detail('6360cf30bf578c6b0ac419fc').text)
print(b.robot_detail('dfff').text)
