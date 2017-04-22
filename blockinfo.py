def get_api_url(hash_value):
    api_url = 'https://blockchain.info/block/{}?format=json'
    return api_url.format(hash_value)
