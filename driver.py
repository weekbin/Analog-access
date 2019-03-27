from selenium import webdriver

from proxy import get_proxy
from useragent import ua_list
import random


def set_driver():
	"""
	configuration of chromedriver
	please check the global environment of chromedriver
	"""
	proxy = get_proxy()
	print(proxy)
	UA = ua = random.sample(ua_list, 1)[0]
	print(UA)
	chromeOptions = webdriver.ChromeOptions()
	chromeOptions.add_argument("--proxy-server=http://" + str(proxy))
	chromeOptions.add_argument('user-agent=' + UA)
	chromeOptions.add_argument('lang=zh_CN.UTF-8')
	chromeOptions.add_argument('--headless')
	chromeOptions.add_argument('--disable-extensions')
	chromeOptions.add_argument('--disable-gpu')
	chromeOptions.add_argument('--no-sandbox')
	return webdriver.Chrome(chrome_options=chromeOptions)
