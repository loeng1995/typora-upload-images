import requests
import sys,os
import re

path = 'F' #此处的 F  更改为你电脑除 C盘以外的硬盘.

URL = 'https://你的上传图片url/upload' #此处填写上传图片的url
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
paths = sys.argv[1:] #获取cmd传入的参数,因为第一个是要执行的py程序,第二个及以后才是图片的绝对路径
remove = False
for i in paths:
    query = re.compile(r'http[s]://')
    if query.match(i):
        resp = requests.get(i,verify=False)
        f = open(f'{path}:/tmp.jpg','wb')
        f.write(resp.content)
        f.close()
        img = open(f'{path}:/tmp.jpg','rb')
        remove = True
    else:
        img = open(i,'rb')
    resp = requests.post(URL,headers=headers,files={'Files':img},verify=False)
    path1 = eval(resp.text)
    url = path1[0]['src']
    newUrl = 'https://你的上传图片url'+url.replace('\\','')
    print(newUrl)
    _ = requests.get(newUrl) #访问一次图片地址,保证记录到admin后台.
    img.close()
    if remove:os.remove(f'{path}:/tmp.jpg')

