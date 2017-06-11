from selenium import webdriver
import time 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
	)
driver = webdriver.PhantomJS(desired_capabilities=dcap)
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
	time.sleep(.7)
	#bitcoin
	bitcoin = driver.find_element_by_xpath("""//*[@id="chart_react"]/div/div[2]/div/div[1]/div/div[1]/div[1]""")
	time.sleep(.7)
	bitcoinhourly = driver.find_element_by_xpath("""//*[@id="chart_react"]/div/div[1]/div[2]/div/div[1]""").click()
	time.sleep(.7)
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
	time.sleep(300)#the amount of seconds it waits to check prices set to one hour	
	count = count + 1
driver.quit()
