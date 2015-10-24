from service.base import BaseService
import requests
import json
import config

class AccountService(BaseService):
    def __init__(self, db, rs):
        super().__init__(db, rs)
        AccountService.inst = self

    def login(self, data={}):
        '''
        username, password
        '''
        url = self.add_client_id(config.BASE_URL + '/login') 
        r = requests.post(url, data=json.dumps(data))
        res = json.loads(r.text)
        token = res.get('token')
        return (None if token else res['message'], token)
