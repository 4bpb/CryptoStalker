import requests
import json
import time
import colorama
from colorama import Fore, Back, Style

def getCurrentTime():
    return time.strftime("%H:%M:%S")
print(Fore.MAGENTA +"Made By @snupreme aka turtl and the pointers/guidance from @yeezylegion and @backdoorcook")
print(Fore.YELLOW +"[{}] Enabling CryptoStalker".format(getCurrentTime()))
req = requests.Session()
while True:
	bitcoin = req.get("https://www.coinbase.com/api/v2/prices/BTC-USD/spot?")
	currentbtc = (bitcoin.json()['data']['amount'])

	bitcoinchangeURL = req.get("https://www.coinbase.com/api/v2/prices/BTC-USD/historic?period=hour")
	A = (float(bitcoinchangeURL.json()['data']['prices'][1]['price']))
	B = (float(bitcoinchangeURL.json()['data']['prices'][-1]['price']))
	bitcoinchange = (A-B)

	ethereum = req.get("https://www.coinbase.com/api/v2/prices/ETH-USD/spot?")
	currenteth =(ethereum.json()['data']['amount'])

	ethereumchangURL = req.get("https://www.coinbase.com/api/v2/prices/ETH-USD/historic?period=hour")
	C = (float(ethereumchangURL.json()['data']['prices'][1]['price']))
	D = (float(ethereumchangURL.json()['data']['prices'][-1]['price']))
	ethereumchange = (C-D)
	print(Fore.CYAN + "########################################")
	print(Fore.YELLOW + "[{}] Current Bitcoin Price is: ${}".format(getCurrentTime(), currentbtc))
	print(Fore.YELLOW + "[{}] Bitcoin Hourly Price Change: ${}".format(getCurrentTime(), bitcoinchange))
	print(" ")
	print(Fore.YELLOW + "[{}] Current ETH Price is: ${}".format(getCurrentTime(), currenteth))
	print(Fore.YELLOW + "[{}] ETH Hourly Price Change: ${} ".format(getCurrentTime(), ethereumchange))
	print(Fore.CYAN + "########################################")
	time.sleep(300)#amount of time (inseconds you would like the bot to wait before pulling prices again) ex: 3600=1hour, 300=5min
