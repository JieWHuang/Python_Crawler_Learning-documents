# import requests
# payload = {'Keywords':'blog:qiyeboy','pageindex':'1'}
# r = requests.get('http://zzk.cnblog.com/s/blogpost',params=payload)
# print(r.url)

# import requests
# import chardet
# r = requests.get('https://www.baidu.com')
# print(chardet.detect(r.content))
# r.encoding = chardet.detect(r.content)['encoding']
# print (r.text)

import requests
r = requests.get('https://www.baidu.com',stream=True)
print (r.raw.read(10))
