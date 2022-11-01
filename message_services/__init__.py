import requests

hostssd = 'https://test.iotdataserver.net'


class Interface_X():
    def __init__(self):
        self.host = hostssd
        self.authorization = 'bearer %s' % self.login()
        self.header = {'Authorization': self.authorization}

    def get_code(self):
        url = '%s/api/auth/certification/captcha2' % self.host
        result = requests.Session().get(url)
        return result.json()['data']['key']

    def get_public_key(self):
        url = '%s/api/auth/certification/publickey' % self.host
        result = requests.Session().get(url)
        return result.json()['code']

    def login(self):
        url = '%s/api/auth/certification/token' % self.host
        code = self.get_code()
        header = {
            'Authorization': 'Basic Y2xpZW50X3dlYjpjbGllbnRfd2ViX3NlY3JldA=='
        }
        data = {
            'username': 'admin',
            'password': 'g9fzqxrdE6GJuNGQPEUuLU4a7AMoh4VdOEdRHb3cHOH4pF7zsOL4LWmcBwffWlEKOObAqpciGlfKMQgCx7WFPA4vcOKwzTw'
                        'js3k30y5EmeRXGDdYJfjJulwyrvGySLy1/NPqcN0fgKgei3ckIeWaNcuJMxfNgL9VV435+k90KPfIgy9NGVkaUr0xd+zGce'
                        '0Bw3DTqOIAK6QvTym3q2YuJib+It9WdSPV6XcK0eoLTV6aSIMk8bStbo/cFO4ZSqwJPc4tQy83n2kBIixykPNIDnstqNZ/R/'
                        'S+W9371FwnSDIaXmm5VJHG6+i9mmv9IRzq7Ee0+3OiK9JdF26c/LJx8w==',
            'grant_type': 'captcha',
            'captcha_key': code,
            'captcha_value': 12345
        }
        result = requests.Session().post(url, headers=header, data=data)
        return result.json()['data']['access_token']

    def post_request(self, url, data=None, param=None, json=None, header=None):
        if header:
            pass
        else:
            header = self.header
        result = requests.Session().post(url=url, data=data, json=json, params=param, headers=header)
        return result

    def get_request(self, url, data=None, param=None, json=None, header=None):
        if header:
            pass
        else:
            header = self.header
        result = requests.Session().get(url=url, data=data, json=json, params=param, headers=header)
        return result

    def delete_request(self, url, data=None, param=None, json=None, header=None):
        if header:
            pass
        else:
            header = self.header
        result = requests.Session().delete(url=url, data=data, json=json, params=param, headers=header)
        return result

    def put_request(self, url, data=None, param=None, json=None, header=None):
        if header:
            pass
        else:
            header = self.header
        result = requests.Session().put(url=url, data=data, json=json, params=param, headers=header)
        return result

    def patch_request(self, url, data=None, param=None, json=None, header=None):
        if header:
            pass
        else:
            header = self.header
        result = requests.Session().patch(url=url, data=data, json=json, params=param, headers=header)
        return result
