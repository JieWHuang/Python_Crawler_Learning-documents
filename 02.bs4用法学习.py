from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'lxml')
# print(soup.prettify())
# print(soup.title)
# print(soup.head)
# print(soup.a)
# print(soup.p)
# print(soup.name)
# print(soup.head.name)
# print(soup.p.attrs)
# print(soup.p['class'])
# print(soup.p.get('class'))
# print(soup.p.string)
# print(soup.head.contents[0])
# for child in soup.body.children:
# 	print(child)
# for child in soup.descendants:
# 	print(child)
# print(soup.find_all('b'))

for tag in soup.find_all(re.compile('^b')):
	print(tag.name)

print(soup.find_all(['a','b']))