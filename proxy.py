import requests

def get_proxy():
	"""
	get the proxy url
	return proxy ip:port
	"""
	PROXY_POOL_URL = 'http://101.132.161.133:5555/random'
	try:
		response = requests.get(PROXY_POOL_URL)
		if response.status_code == 200:
			return response.text
	except ConnectionError:
		return None