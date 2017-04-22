"""Parse Bitcoin Block Information from blockchain.info API
"""
import json
from urllib.request import urlopen

class BlockInfo():
    def __init__(self, hash_value):
        self.api_url = self.get_api_url(hash_value)
        self.block = self.get_block_from_api(self.api_url)
        self.n_tx = self.get_n_tx(self.block)
        self.avg_tx_value = self.get_avg_tx_value(self.n_tx, self.block['tx'])

    def get_api_url(self, hash_value):
        api_url = 'https://blockchain.info/block/{}?format=json'
        return api_url.format(hash_value)

    def get_block_from_api(self, api_url):
        data = urlopen(api_url).read().decode()
        return json.loads(data)

    def get_n_tx(self, block):
        return block['n_tx']

    def get_avg_tx_value(self, n_tx, transactions):
        value = 0
        for tx in transactions:
            for out in tx['out']:
                value += out['value']

        return round(value / n_tx * 1e-8, 8)
