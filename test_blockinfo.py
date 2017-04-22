from blockinfo import get_api_url

def test_get_api_url():
    hash_value = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'

    assert get_api_url(hash_value) == 'https://blockchain.info/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f?format=json'
