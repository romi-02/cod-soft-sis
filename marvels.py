from hashlib import md5
from requests import get 
from datetime import datetime 

class RestMarvel:
    timestamp = datetime.now().strftime('%Y-%d%H:%M:%S')
    pub_key = '721bd65ff8f8aa9560c39546beee5c4e'
    priv_key = '8d52b9b6dd2507896f479c3bba71711977aa2a63'
    
    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params = {'ts':self.timestamp,'apikey':self.pub_key,'hash':self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters', params=params)
        
        data = results.json()
        print(data)
        print(data['status'])

mv = RestMarvel()
mv.get_heroes()

                                         