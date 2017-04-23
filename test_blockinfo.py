import math
import pytest
from blockinfo import BlockInfo
from urllib.error import HTTPError

@pytest.fixture(scope='module')
def single_tx_block():
    hash_value = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
    return BlockInfo(hash_value)

@pytest.fixture(scope='module')
def multiple_tx_block():
    hash_value = '0000000000000e102232eeb35175920438b8d8de12cab20f3e4d5b6e56dbca95'
    return BlockInfo(hash_value)

def test_invalid_hash_value():
    hash_value = 'invalid000000e102232eeb35175920438b8d8de12cab20f3e4d5b6e56dbca95'
    with pytest.raises(HTTPError) as excinfo:
        BlockInfo(hash_value)
    # When hash value is invalid, response code is 500 error.
    excinfo.match(r'.*500.*')

def test_get_api_url(single_tx_block):
    assert single_tx_block.api_url == 'https://blockchain.info/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f?format=json'

def test_n_tx(single_tx_block, multiple_tx_block):
    assert single_tx_block.n_tx == 1
    assert multiple_tx_block.n_tx == 9

def test_avg_tx_value(single_tx_block, multiple_tx_block):
    assert math.isclose(single_tx_block.avg_tx_value, 50, rel_tol=1e-8)
    assert math.isclose(multiple_tx_block.avg_tx_value, 39.65358258, rel_tol=1e-8)

def test_avg_tx_fee(single_tx_block, multiple_tx_block):
    assert math.isclose(single_tx_block.avg_tx_fee, 0, rel_tol=1e-8)
    assert math.isclose(multiple_tx_block.avg_tx_fee, 0.00044444, rel_tol=1e-8)

def test_avg_tx_size(single_tx_block, multiple_tx_block):
    assert single_tx_block.avg_tx_size == 204
    assert multiple_tx_block.avg_tx_size == 460

def test_tx_inputs(single_tx_block, multiple_tx_block):
    tx_inputs = single_tx_block.tx_inputs
    assert len(tx_inputs) == 1

    tx_inputs = multiple_tx_block.tx_inputs
    assert len(tx_inputs) == 9
    tx_input = tx_inputs[5]
    assert tx_input['hash'] == 'dce1b8cdb8cf06915c217c18fd28ffcbca90e70b280651302b2fdd47748ca25b'
    assert len(tx_input['inputs']) == 2

def test_tx_outputs(single_tx_block, multiple_tx_block):
    tx_outputs = single_tx_block.tx_outputs
    assert len(tx_outputs) == 1

    tx_outputs = multiple_tx_block.tx_outputs
    assert len(tx_outputs) == 9
    tx_output = tx_outputs[0]
    assert tx_output['hash'] == 'c81d11dd31a8f37824d81290a983b8d815fd17def166f3a4b722604639d70011'
    assert len(tx_output['outputs']) == 46
