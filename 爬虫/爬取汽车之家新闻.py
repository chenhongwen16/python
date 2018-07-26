import requests
from bs4 import BeautifulSoup

#下载页面
ret = requests.get(url='https://www.autohome.com.cn/news/')
ret.encoding = 'gbk'
print(ret.text)

#解析：获取想要的制定内容beautifulsoup4
soup = BeautifulSoup(ret.text,'html.parser')#lxml
div = soup.find(name='div',id='auto-channel-lazyload-article')

li_list = div.find_all(name='li')
print(li_list)

for li in li_list:
    h3=li.find(name='h3')
    if not h3:continue
    p = li.find(name = 'p')
    a = li.find('a')

    img = li.find('img')
    src = img.get('src')
    file_name = src.split('__')[1]
    ret_img = requests.get(url="https:"+src)
    with open(file_name,'wb') as f:
        f.write(ret_img.content)






    print(h3.text,a.get('href'))
    print(p.text)
    print('='*15)
