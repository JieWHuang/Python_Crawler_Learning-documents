import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def get_info(url):
	time.sleep(2)
	wb_data = requests.get(url,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	title = soup.select('div.pho_info > h4 > em')[0].text
	addr = soup.select('div.pho_info > p')[0].get('title')
	price = soup.select('div.day_l')[0].text
	img = soup.select('img[id="curBigImage"]')[0].get('src')
	owner_img =  soup.select('div.member_pic > a > img')[0].get('src')
	if soup.select('div.member_ico'):
		owner_sex = "男"
	else:
		owner_sex = "女"
	owner_name = soup.select('div.w_240 > h6 > a')[0].text


	data = {
		'标题':title,
		'地址':addr,
		'日租金':price,
		'房源图片链接':img,
		'房东图片链接':owner_img,
		'房东性别':owner_sex,
		'房东名字':owner_name
	}
	print(data)


def get_link_info(url):
	wb_data = requests.get(url,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	hrefs_list = soup.select('ul > li > a[target="_blank"]')
	for href in hrefs_list:
		link = href.get('href')
		get_info(link)

def main():
	urls = ['http://gz.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,2)]
	links = {}
	for single_url in urls:
		get_link_info(single_url)

main()
