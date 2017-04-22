"""Parse Bitcoin Block Information from blockchain.info API
"""

class BlockInfo():
    def __init__(self, hash_value):
        self.api_url = self.get_api_url(hash_value)

    def get_api_url(self, hash_value):
        api_url = 'https://blockchain.info/block/{}?format=json'
        return api_url.format(hash_value)
