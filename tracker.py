"""
Handles URL requests to hiveon server
"""
import urllib.request, json
from urllib.parse import urlparse, urlunsplit

PROTO = "https"
SERVER = "hiveon.net"
BASE_API = "api/v1/stats/miner"
WALLET = "a438abea8bfb8855adcb08d4a369f751148522ae"
COIN = "ETH"
ENDPOINT = "workers"

# "https://hiveon.net/api/v1/stats/miner/
API_STRING = urlunsplit((PROTO, SERVER, BASE_API, '', ''))
# "https://hiveon.net/api/v1/stats/miner/a438abea8bfb8855adcb08d4a369f751148522ae
WALLET_STR = "/".join((API_STRING, WALLET))
# https://hiveon.net/api/v1/stats/miner/a438abea8bfb8855adcb08d4a369f751148522ae/ETH/
COIN_STR = "/".join((WALLET_STR, COIN))
# https://hiveon.net/api/v1/stats/miner/a438abea8bfb8855adcb08d4a369f751148522ae/ETH/workers
WORKERS_ENDPOINT_URL = "/".join((COIN_STR, ENDPOINT))

with urllib.request.urlopen(WORKERS_ENDPOINT_URL) as url:
    data = json.loads(url.read().decode())
    for workername,workerstats in data['workers'].items():
        print(workername, ",", workerstats['sharesStatusStats']['validCount'])