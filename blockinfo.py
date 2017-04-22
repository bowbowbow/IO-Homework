"""Parse Bitcoin Block Information from blockchain.info API
"""
import json
from urllib.request import urlopen

class BlockInfo():
    def __init__(self, hash_value):
        self.api_url = self.get_api_url(hash_value)
        self.block = self.get_block(self.api_url)
        self.n_tx = 1

    def get_api_url(self, hash_value):
        api_url = 'https://blockchain.info/block/{}?format=json'
        return api_url.format(hash_value)

    def get_block(self, api_url):
        data = urlopen(api_url).read().decode()
        return json.loads(data)
