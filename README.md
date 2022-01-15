# wscrpy
web scraping and data parsing library
-------------------------------------
installation
---------------------------------------
pip install wscrpy 
-----------------------
<img src="https://i.ibb.co/8bb3Dvf/2022-01-14-101645.jpg" > </img>
#### import Main_request from wscrpy
from wscrpy import Main_request
#### http headers
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'}
#### Main request
c  = Main_request("https://docs.python-requests.org/en/latest/user/quickstart/")
##### start get request
r = c.mkgreq(headers_=headers)
#### start parsing 
soup = c.parser(r.content)
#### parsing webpage title
s = soup.title
#### prettify print
c.pprt(s)
#### find all links
finder_result = c.finder(soup,findall='a')
#### print all links herf
for i in finder_result:
	print(i['href'])
