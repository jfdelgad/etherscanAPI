# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 20:21:25 2018
@author: Jaime Delgado
"""

import requests

class etherscan:
    def __init__(self, apikey, network):
        self.network = network
        self.apikey = apikey
        if network=='mainnet':
            self.apipath = 'https://api.etherscan.io/api?'
        else:
            self.apipath = 'https://api' + '-' + network + '.etherscan.io/api?' 
           
    
    # Acounts  API   
    def getBalance(self, address):
        payload = {'module':'account', 'action':'balance', 'address':address, 'tag':'latest', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']
    
    def getBalanceMulti(self, address):
        payload = {'module':'account', 'action':'balancemulti', 'address':','.join(address), 'tag':'latest', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']
    
    def getTransactions(self, address, fromblock, toblock):
        payload = {'module':'account', 'action':'txlist', 'address':address, 'startblock':fromblock, 'endblock':toblock, 'sort':'asc', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']
    
    def getInternalTransactionsByAddress(self, address, fromblock, toblock):
        payload = {'module':'account', 'action':'txlistinternal', 'address':address, 'startblock':fromblock, 'endblock':toblock, 'sort':'asc', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getInternalTransactionsByTxHash(self, txhash, fromblock, toblock):
        payload = {'module':'account', 'action':'txlistinternal', 'txhash':txhash, 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']
    
    def getERC20TransfersByAddress(self, address, fromblock, toblock):
        payload = {'module':'account', 'action':'tokentx', 'address':address, 'startblock':fromblock, 'endblock':toblock, 'sort':'asc', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']
    
    def getERC20TransfersByContract(self, contractAddress, address, fromblock, toblock):
        payload = {'module':'account', 'action':'tokentx', 'address':address,  'contractaddress':contractAddress, 'startblock':fromblock, 'endblock':toblock, 'sort':'asc', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getMinedBlocks(self, address):
        payload = {'module':'account', 'action':'getminedblocks', 'address':address,  'blocktype':'blocks', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']



    # Contracts API
    def getContractABI(self, address):
        payload = {'module':'contract', 'action':'getabi', 'address':address, 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getSourceCode(self, address):
        payload = {'module':'contract', 'action':'getsourcecode', 'address':address, 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']



    # Transactions API
    def getReceiptStatus(self, txhash):
        payload = {'module':'transaction', 'action':'gettxreceiptstatus', 'txhash':txhash, 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']
    
    def getContractTxStatus(self, txhash):
        payload = {'module':'transaction', 'action':'getstatus', 'txhash':txhash, 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']
    
    
    
    # Blocks
    def getBlockRewards(self, blockNumber):
        payload = {'module':'block', 'action':'getblockreward', 'blockno':blockNumber, 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    
    
    # GETH/PARITY Proxy API
    def getBlockNumber(self):
        payload = {'module':'proxy', 'action':'eth_BlockNumber', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getBlockByNumber(self, number):
        payload = {'module':'proxy', 'action':'eth_getBlockByNumber', 'tag':hex(number), 'boolean':'true', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getBlockTransactionCountByNumber(self, number): 
        payload = {'module':'proxy', 'action':'eth_getBlockTransactionCountByNumber', 'tag':hex(number), 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getUncleByBlockNumberAndIndex(self, number, index): 
        payload = {'module':'proxy', 'action':'eth_getUncleByBlockNumberAndIndex', 'tag':hex(number), 'index':hex(index), 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getTransactionByHash(self, txhash):
        payload = {'module':'proxy', 'action':'eth_getTransactionByHash', 'txhash':txhash, 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']
        
    def getTransactionByBlockNumberAndIndex(self, number, index):
        payload = {'module':'proxy', 'action':'eth_getTransactionByBlockNumberAndIndex', 'tag':hex(number), 'index':hex(index), 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getTransactionCount(self, address):
        payload = {'module':'proxy', 'action':'eth_getTransactionCount', 'address':address,'tag':'latest', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def sendRawTransaction(self, signedTx):
        payload = {'module':'proxy', 'action':'eth_sendRawTransaction', 'hex':signedTx, 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getTransactionReceipt(self, txhash):
        payload = {'module':'proxy', 'action':'eth_getTransactionReceipt', 'txhash':txhash, 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def call(self, to, data):
        payload = {'module':'proxy', 'action':'eth_call', 'tag':'latest', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getCode(self, address):
        payload = {'module':'proxy', 'action':'eth_getCode', 'address':address, 'tag':'latest', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getStorageAt(self, address, position):
        payload = {'module':'proxy', 'action':'eth_getStorageAt', 'address':address, 'position':hex(position), 'tag':'latest', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def gasPrice(self):
        payload = {'module':'proxy', 'action':'eth_gasPrice', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def estimateGas(self, to, value, gasprice, gas):
        payload = {'module':'proxy', 'action':'eth_estimateGas', 'to':to, 'value':hex(value), 'gasPrice':hex(gasprice), 'gas':hex(gas),  'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']



    # EVENT logs
    def getLogs(self, fromBlock, toBlock, address, topics, topicsOperator): 
        payload = {'module':'logs', 'action':'getLogs', 'fromBlock':fromBlock, 'toBlock':toBlock, 'apikey':self.apikey}
        payload.update(dict(topics,**topicsOperator))
        return requests.get(self.apipath, params=payload).json()['result']
 

    
    # Token
    def getTokenTotalSupply(self, contractAddress):
        payload = {'module':'account', 'action':'tokensupply', 'contractaddress':contractAddress, 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getTokenBalance(self, address, contractAddress):
        payload = {'module':'account', 'action':'tokenbalance', 'contractaddress':contractAddress, 'address':address, 'tag':'latest', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']
    


    # Stats
    def getEtherSupply(self):
        payload = {'module':'stats', 'action':'ethsupply', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']

    def getEtherPrice(self):
        payload = {'module':'stats', 'action':'ethprice', 'apikey':self.apikey}
        return requests.get(self.apipath, params=payload).json()['result']
    
