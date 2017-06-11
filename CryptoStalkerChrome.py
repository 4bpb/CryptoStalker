from selenium import webdriver
import time 
driver = webdriver.Chrome()
def getCurrentTime():
    return time.strftime("%H:%M:%S")
url = 'https://coinbase.com/charts/'
print("Made By @snupreme aka turtl")
print("[{}] Enabling CryptoStalker".format(getCurrentTime()))
driver.get(url)
var = 99999999 
count = 0                                         

while count < var:
	driver.find_element_by_xpath("""//*[@id="chart_react"]/div/div[1]/div[1]/div/div[1]""").click()
	#bitcoin
	bitcoin = driver.find_element_by_xpath("""//*[@id="chart_react"]/div/div[2]/div/div[1]/div/div[1]/div[1]""")
	time.sleep(.5)
	bitcoinhourly = driver.find_element_by_xpath("""//*[@id="chart_react"]/div/div[1]/div[2]/div/div[1]""").click()
	time.sleep(.3)
	bitcoinchange = driver.find_element_by_xpath("""//*[@id="chart_react"]/div/div[2]/div/div[1]/div/div[2]/div[1]""")
	print("########################################")
	print("[{}] Current Bitcoin Price is".format(getCurrentTime()), bitcoin.text)
	print("Bitcoin Hourly Price Change: "+bitcoinchange.text)
	time.sleep(2)
	print(" ")
	#ether
	driver.find_element_by_xpath("""//*[@id="chart_react"]/div/div[1]/div[1]/div/div[2]/div/h4""").click()
	ethereum = driver.find_element_by_xpath("""//*[@id="chart_react"]/div/div[2]/div/div[1]/div/div[1]/div[1]""")
	time.sleep(.5)
	etherphourly = driver.find_element_by_xpath("""//*[@id="chart_react"]/div/div[1]/div[2]/div/div[1]""").click()
	etherchange = driver.find_element_by_xpath("""//*[@id="chart_react"]/div/div[2]/div/div[1]/div/div[2]/div[1]""")
	print("[{}] Current Ethereum Price is".format(getCurrentTime()), ethereum.text)
	print("Ethereum Hourly Price Change: "+etherchange.text)
	print("########################################")
	time.sleep(3600)#the amount of seconds it waits to check prices set to one hour	
	count = count + 1
driver.quit()
