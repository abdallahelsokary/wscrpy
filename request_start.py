"""
== wscrp v01 == 
Author : Abdallah Elsokary
https://twitter.com/abdallahelsoka1
https://www.youtube.com/channel/UCpis91Zi0N-CGjqjFXuRt4w
"""
import requests
import sys
from bs4 import BeautifulSoup

class Main_request:
	# initialize class 
	def __init__(self,url):
		self.url = url

	# get request 
	def mkgreq(self,params_= None ,  headers_ = None , cookies_ = None):
		try :
			if params_ != None and headers_ == None and cookies_ == None:
				r = requests.get(self.url,params=params_)
			elif headers_ != None and params_ == None and cookies_ == None:
				r = requests.get(self.url,headers=headers_)
			elif params_ != None and headers_ != None and cookies_ == None:
				r = requests.get(self.url,params=params_,headers=headers_)
			elif params_ != None and headers_ != None and cookies_ != None:
				c_jar = requests.cookies.RequestsCookieJar()
				c_jar.set(cookies_)
				r = requests.get(self.url,params=params_,headers=headers_,cookies=c_jar)
			else:
				r = requests.get(self.url)
			return r
		except Exception as e:
			print(e)
			sys.exit(1)

	# post request

	def mkpreq(self,data_ = None , headers_ = None , cookies_ = None):
		try :
			if data_ != None and headers_ == None and cookies_ == None:
				r = requests.post(self.url,data=data_)
			elif data_ != None and headers_ != None and cookies_ == None:
				r = requests.post(self.url,data=data_,headers=headers_)
			elif data_ != None and headers_ != None and cookies_ != None:
				c_jar = requests.cookies.RequestsCookieJar()
				c_jar.set(cookies_)
				r = requests.post(self.url,data=data_,headers=headers_,cookies=c_jar)
			return r
		except Exception as e:
			print(e)
			sys.exit(1)

	# html parser

	def parser(self,res):
		try:
			soup = BeautifulSoup(res,'html.parser')
			return soup
		except Exception as e:
			print(e)
			sys.exit(1)

	# finder
	def finder(self,soup,findall = None , find = None):
		try:
			if findall != None and find == None:
				res = soup.find_all(findall)
				return res
			elif findall == None and find != None:
				res = soup.find(find)
				return res 
		except Exception as e:
			print(e)
			sys.exit(1)

	# prettify print

	def pprt(self,soup):
		try:
			print(soup.prettify())
		except Exception as e:
			print(e)
			sys.exit(0)




"""
# http headers

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'}
# Main request
c  = Main_request("https://docs.python-requests.org/en/latest/user/quickstart/")
# start get request
r = c.mkgreq(headers_=headers)
# start parsing 
soup = c.parser(r.content)
# parsing webpage title
s = soup.title
# prettify print
c.pprt(s)
# find all links
finder_result = c.finder(soup,findall='a')
# print all links herf
for i in finder_result:
	print(i['href'])
"""