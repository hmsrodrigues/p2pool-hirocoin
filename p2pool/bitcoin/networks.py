import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc
from operator import *


@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

nets = dict(

    hirocoin=math.Object(
        P2P_PREFIX='fec3b9de'.decode('hex'),
        P2P_PORT=4343,
        ADDRESS_VERSION=40,
        RPC_PORT=3343,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'hirocoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),                           
        SUBSIDY_FUNC=lambda height: 400*100000000 >> (height + 1)//840000,
        BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
        BLOCK_PERIOD=60, # s
        SYMBOL='HIRO',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Hirocoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Hirocoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.hirocoin'), 'hirocoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.hirocoin.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.hirocoin.org/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.hirocoin.org/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1), 
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),



)
for net_name, net in nets.iteritems():
    net.NAME = net_name
