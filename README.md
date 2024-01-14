# Typora搭配Telegraph Image免费图床实现插入图片自动转换成Url.

>作者:Loeng1995
>
>源码已上传github:[点击此处跳转至github](https://github.com/loeng1995/typora-upload-images)
>
>联系邮箱:loeng1995@loeng.top
>
>◎转载请注明出处!!!

>- 准备项目: Cloudflare账号,GitHub账号. (其他图床也可以.)
>
>- Typora
>
>- 理论有其他图床也是可以的,而且Typora有支持的插件PicGo上传,但是我没有用过,不知道具体怎么操作.  
>
>  (本教程只以自定义命令为主要实现.需具备一定的编程知识,任何一种都可以.)

---

## 1. Telegraph Image图床

#### 有其他的图床也可以忽略这一步

- 1.1 免费图床的搭建不在本文的范畴,开源地址:[https://github.com/cf-pages/Telegraph-Image](https://github.com/cf-pages/Telegraph-Image)
- 1.2 根据项目中的README文档完成图床的搭建.

## 2.Typora 自定义命令

- 根据下图依次点击, 文件→偏好设置→图像→上传服务设定→自定义命令.

  根据`验证图片上传选项`验证得知, 当插入图片时,会自动执行设置的命令,并且传递一个字符串参数(图片缓存文件的绝对路径).

  那么就可以自己编写一个`py`文件来实现图片的自动上传,

  

  ![image-20240108231655338](https://images.loeng.top/file/664201ccb199cdb372f8e.png)

- Typora解析是否上传成功的验证机制是是否输出一个url连接并访问.

  下图显示验证成功.

  ![7bfa985cc31488a2f93ec](https://images.loeng.top/file/9bacfd0ef004d655c3bd9.jpg)

  那么就可以在控制台(cmd)输出上传后的url连接即可.

## 3. 编写py文件(其他编程语言也可以)

- 其重要的部分是获取上传图片的api.并通过python自动上传图片,

  图片从`cmd`传入的参数获取.并且在控制台`cmd`输出图片url即可.

  ```python
  import requests
  import sys
  
  
  URL = 'https://你的图床地址' #此处填写上传图片的url
  headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
  }
  paths = sys.argv[1:] #获取cmd传入的参数,因为第一个是要执行的py程序,第二个及以后才是图片的绝对路径
  for i in paths:
      img = open(i,'rb')
      resp = requests.post(URL,headers=headers,files={'Files':img})
      path1 = eval(resp.text)
      url = path1[0]['src']
      newUrl = 'https://你的图床地址'+url.replace('\\','')
      print(newUrl)
      _ = requests.get(newUrl) #访问一次图片地址,保证记录到admin后台.
      img.close()
  ```

  

- 完成以上操作,并且设置插入图像时应用以上规则,即可实现typora自动上传图片并转换为url地址.

  ![image-20240108233437738](https://images.loeng.top/file/0aec0702e5a08203a66d3.png)

- 当然了,网络位置的你也可以上传到自己的图床,防止图片丢失.

  这个需要你自己去实现,在此只提供思路.

  - 插入网络位置的图片传入的参数是`url`并非图片的路径.
  - 你可以判断参数的参数是否是`url`.(是否包含`http`|`https`字样)
  - 是`url`,则编写下载程序,并上传到自己的图床.

---

以上就是`Typora`自定义命令的使用,

谢谢观看!!请点一下赞再走!!!

​	
