# etherscanAPI
A python wrapper for EtherScan API. (unofficial)

This library allows to interface with etherscan. It implements the requests to the modules:
* Accounts.
* Transactions.
* GETH / PARITY Proxy.
* Logs.

All methods return the field *Result* of the request as described in [etherscan website](https://etherscan.io/apis).

## Usage:
``` python
from ethersacanAPI import etherscan
myapi = etherscan('myapikey','networkname')
```
Use networkname ='' for mainnet.<br>
Use networkname ='ropsten' for Ropsten.<br>
Use networkname ='rinkeby' for Rinkeby.<br>
<br>

## Methods Description:

### Accounts: [Details](https://etherscan.io/apis#accounts)
* **getBalance(address)**<br>
Get Ether Balance for a single Address.<br>
 
* **getBalanceMulti(address)**<br>
Get Ether Balance for multiple Addresses in a single call.<br>
Address must be a list of addresses.<br>

* **getTransactions(address, fromblock, toblock)**<br>
Get a list of 'Normal' Transactions By Address.<br>

* **getInternalTransactionsByAddress(address, fromblock, toblock)**<br>
Get a list of 'Internal' Transactions by Address.<br>

* **getInternalTransactionsByTxHash(txhash, fromblock, toblock)**<br>
 Get "Internal Transactions" by Transaction Hash.<br>
  
* **getERC20TransfersByAddress(address, fromblock, toblock)**<br>
Get a list of "ERC20 - Token Transfer Events" by Address.<br>
    
* **getERC20TransfersByContract(contractAddress, address, fromblock, toblock)**<br>
Get a list of "ERC20 - Token Transfer Events" by account Address and contract address.<br>

* **getMinedBlocks(address)**<br>
Get list of Blocks Mined by Address.<br><br>



### Transactions: [Details](https://etherscan.io/apis#transactions)
* **getReceiptStatus(txhash)**<br>
Return the status of a transaction with transaction-hash = txhash.<br><br>



### Geth/Parity proxy: [Details](https://etherscan.io/apis#proxy)
* **getBlockNumber()**<br>
Returns the number of most recent block.<br>

* **getBlockByNumber(number)**<br>
Returns information about a block by block number.<br>

* **getBlockTransactionCountByNumber(number)**<br>
Returns the number of transactions in a block from a block matching the given block number.<br>

* **getUncleByBlockNumberAndIndex(number, index)**<br>
Returns information about a uncle by block number.<br>

* **getTransactionByHash(txhash)**<br>
Returns the information about a transaction requested by transaction hash.<br>

* **getTransactionByBlockNumberAndIndex(number, index)**<br>
Returns information about a transaction by block number and transaction index position.<br>

* **getTransactionCount(address)**<br>
Returns the number of transactions sent from an address.<br>

* **sendRawTransaction(signedTx)**<br>
Returns the receipt of a transaction by transaction hash.<br>

* **def getTransactionReceipt(txhash)**<br>
Creates new message call transaction or a contract creation for signed transactions.<br>

* **call(to, data)**<br>
Executes a new message call immediately without creating a transaction on the blockchain.<br>

* **getCode(address)**<br>
Returns code at a given address.<br>

* **getStorageAt(address, position)**<br>
Returns the value from a storage position at a given address.<br>

* **gasPrice()**<br>
Returns the current price per gas in wei.<br>

* **estimateGas(to, value, gasprice, gas)**<br>
Makes a call or transaction, which won't be added to the blockchain and returns the used gas, which can be used for estimating the used gas.<br><br>


### Logs: [Details](https://etherscan.io/apis#logs)
* **getLogs(self, fromBlock, toBlock, address, topics, topicsOperator)**<br>
`topics` is a dictionary with possible entries `topic0`, `topic1`, `topic2`<br>
`topicsOperator` is a dictionary with possible value: `topics0_1_op`, `topics0_2_op`, and `topics1_2_op`.<br>
It determines the type of filter applied to the topics. See the exemples below for details of usage.



## Examples:

```python
from etherscanAPI import etherscan

apikey = 'yourAPIkey'
myapi = etherscan(apikey, '') #

# Get the balance of an account
address = '0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae'
myapi.getBalance(address)


# Get contract logs at address='0x33990122638b9132ca29c723bdf037f1a891a70c' with topic0 = '0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545', fromblock:379224 to block 4000000
# topicsOperator should be an empty dictionary if only one topic is used.
topics = {'topic0':'0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545'}
topicsOperator = {}
myapi.getLogs(379224,400000,'', topics, topicsOperator)


# Get contract logs with using two topics
# topicsOperator is empty if only one topic is used
topics = {'topic0':'0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545',
          'topic1':'0x72657075746174696f6e00000000000000000000000000000000000000000000'}
topicsOperator = {'topic0_1_opr':'and'}
myapi.getLogs(379224,400000,'0x33990122638b9132ca29c723bdf037f1a891a70c', topics, topicsOperator)

```

