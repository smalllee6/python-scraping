import requests
def getText(url):
	try:
		r=requests.get(url)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		print(r.text)
	except:
		print('we could not find text')
url='https://bbs.hupu.com/'
getText(url)
