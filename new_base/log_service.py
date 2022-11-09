import hashlib
import threading
import time

from new_base.resourcesync_service import *
import base64
from hashlib import *


class Log_list(Resourcesync_service_interface):
    def list_log(self, filter):
        url = '%s/api/log/operations' % self.host
        data = {
            '$filter': filter
        }
        result = self.get_request(url=url, param=data)
        return result

b = Log_list()
print(b.list_log("app eq platform-resourcesync").text)
