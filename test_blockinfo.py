from blockinfo import BlockInfo

def test_get_api_url():
    hash_value = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
    block_info = BlockInfo(hash_value)

    assert block_info.api_url == 'https://blockchain.info/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f?format=json'

def test_n_tx():
    hash_value = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
    block_info = BlockInfo(hash_value)
    assert block_info.n_tx == 1

    hash_value = '0000000000000e102232eeb35175920438b8d8de12cab20f3e4d5b6e56dbca95'
    block_info = BlockInfo(hash_value)
    assert block_info.n_tx == 9
