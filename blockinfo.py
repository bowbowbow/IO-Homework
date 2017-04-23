"""Parse Bitcoin Block Information from blockchain.info API
"""
import sys
import json
import argparse
from urllib.request import urlopen
from urllib.error import HTTPError
from pprint import pprint

class BlockInfo():
    def __init__(self, hash_value):
        self.api_url = self.get_api_url(hash_value)
        self.block = self.get_block_from_api(self.api_url)
        self.n_tx = self.get_n_tx(self.block)
        self.avg_tx_value = self.get_avg_tx_value(self.n_tx, self.block['tx'])
        self.avg_tx_fee = self.get_avg_tx_fee(self.n_tx, self.block['fee'])
        self.avg_tx_size = self.get_avg_tx_size(self.n_tx, self.block['tx'])
        self.tx_inputs = self.get_tx_inputs(self.block['tx'])

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

    def get_avg_tx_fee(self, n_tx, fee):
        return round(fee / n_tx * 1e-8, 8)

    def get_avg_tx_size(self, n_tx, transactions):
        size = 0
        for tx in transactions:
            size += tx['size']

        return round(size / n_tx)

    def get_tx_inputs(self, transactions):
        inputs = []
        for tx in transactions:
            tx_input = {}
            tx_input['hash'] = tx['hash']
            tx_input['inputs'] = tx['inputs']

            inputs.append(tx_input)

        return inputs

    def get_tx_info(self):
        tx_info = {}
        tx_info['n_tx'] = self.n_tx
        tx_info['avg_tx_value'] = self.avg_tx_value
        tx_info['avg_tx_fee'] = self.avg_tx_fee
        tx_info['avg_tx_size'] = self.avg_tx_size

        return tx_info

if __name__ == '__main__':
    parser = argparse.ArgumentParser();
    parser.add_argument('hash_value', help='Bitcoin block hash')
    parser.add_argument("input_or_output",
                        nargs='?',
                        choices=['input', 'output'],
                        help="Print inputs or outputs of the transactions")
    args = parser.parse_args();

    input_or_output = ''

    if args.input_or_output is not None:
        input_or_output = args.input_or_output

    try:
        block_info = BlockInfo(args.hash_value)

        if input_or_output == 'input':
            pprint(block_info.tx_inputs)
        elif input_or_output == 'output':
            pass
        else:
            tx_info = block_info.get_tx_info()
            print('Number of Transactions: {}'.format(tx_info['n_tx']))
            print('Average Value of Transactions: {:.8f} BTC'.format(tx_info['avg_tx_value']))
            print('Average Fee of Transactions: {:.8f} BTC'.format(tx_info['avg_tx_fee']))
            print('Average Size of Transactions: {} bytes'.format(tx_info['avg_tx_size']))

    except HTTPError as err:
        if err.getcode() == 500:
            print('Block hash is invalid')
        else:
            print('Unexpected Error: {}'.format(sys.exc_info()[0]))
            raise
