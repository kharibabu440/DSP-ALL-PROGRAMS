import requests
from bs4 import BeautifulSoup as bsp
req=requests.get('https://www.python.org/')
soup=bsp(req.content,'html.parser')
p=soup.find_all('p')
for i in p:
    print(i.get('text'))
