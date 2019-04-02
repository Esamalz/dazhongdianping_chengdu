import requests
from bs4 import BeautifulSoup
def get_html(url):
   headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
   resp=requests.get(url,headers=headers).text
   return resp
def html_parse():
   for url in allpages():
      soup=BeautifulSoup(get_html(url),'lxml')
      allname=soup.find_all('div',class_='tit')
      names=[a.find('h4')for a in allname]
      for b in names:
         name=b.get_text()
         for result in zip(name,):
            result=str(name)
         f.writelines(result+'\n')
      
def allpages():
   baseurl='http://www.dianping.com/shenyang/ch10/g109p'#找到你需要的网页
   urllist=[]
   for page in range(1,8,1):#一共有n页，把8改成n+1
      allurl=baseurl+str(page)
      urllist.append(allurl)
   return urllist
filename='shenyangsushi.txt'#电脑中保存的文件名
f=open(filename,'w',encoding='utf-8')
html_parse()
f.close()
print('ok!')

