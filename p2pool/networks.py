from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(

    hirocoin=math.Object(
        PARENT=networks.nets['hirocoin'],
        SHARE_PERIOD=15, # seconds
        NEW_SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=30, # blocks
        NEW_SPREAD=30, # blocks
        IDENTIFIER='496247d46a02b228'.decode('hex'),
        PREFIX='5685a273806822dd'.decode('hex'),
        P2P_PORT=8343,
        MIN_TARGET=4,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=7343,
        BOOTSTRAP_ADDRS='p2pools.plentygadget.com hiro.qemulab.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-hic',
        VERSION_CHECK=lambda v: True,
    ),
	darkcoin=math.Object(
        PARENT=networks.nets['darkcoin'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//15, # shares
        REAL_CHAIN_LENGTH=24*60*60//15, # shares
        TARGET_LOOKBEHIND=200, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=30, # blocks
        IDENTIFIER='ef05d164bbcd7ed1'.decode('hex'),
        PREFIX='3966e45ab1ed2db9'.decode('hex'),
        P2P_PORT=8334,
        MIN_TARGET=4,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=7334,
        BOOTSTRAP_ADDRS='drk.altmine.net p2pool.plentygadget.com drk2.altmine.net drk3.altmine.net asia01.poolhash.org asia02.poolhash.org q30.qhor.net poulpe.nirnroot.com drk.p2pool.n00bsys0p.co.uk darkcoin.kicks-ass.net darkcoin.fr cryptohasher.net coinminer.net drk.coinquarry.net drk.kopame.com 54.186.8.140 rebootcamp.de'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-drk',
        VERSION_CHECK=lambda v: v >= 91001,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
