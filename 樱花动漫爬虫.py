import requests,openpyxl
from bs4 import BeautifulSoup

b1=openpyxl.Workbook()
b2=b1.active

b2['A1']='名字'
b2['B1']='集数+类型'
b2['C1']='简介'

for o in range(3):#在range里更改想要保存的页数
    url='http://www.imomoe.in/so.asp?page='+str(o+1)

    a1=requests.get(url)
    a1.encoding = 'gbk'
    a2=BeautifulSoup(a1.text,'html.parser')
    a3=a2.find('div',class_='pics').find_all('li')
    for i in a3:
        aaa=i.find('h2').find('a')
        bbb=i.find_all('span')
        ccc=i.find('p')
        name=aaa['title']
        bbb2=bbb[1]
        jishu=bbb2.text
        jianjie=ccc.text
        try:
            b2.append([name,jishu,jianjie])
        except openpyxl.utils.exceptions.IllegalCharacterError:
            pass
        continue
        
b1.save('动漫.xlsx')