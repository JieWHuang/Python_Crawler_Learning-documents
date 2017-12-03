import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

base_url = 'https://www.qiushibaike.com/8hr/page/'

for num in range(1,5):
	print('第{}页'.format(num))

	r = requests.get(base_url + str(num), headers = headers)
	content = r.text
	soup = BeautifulSoup(content, 'lxml') 

	divs = soup.find_all(name = 'div' ,attrs={"class" : re.compile(r"article block untagged mb15 typs_[A-z]{0,4}")});

	for div in divs:
		if div.find_all(class_ = 'thumb'):
			continue
		joke = div.span.get_text()
		print(joke)
		print('--------------------')
		