import requests
from bs4 import BeautifulSoup as bsp
req=requests.get('https://www.python.org/')
soup=bsp(req.content,'html.parser')
h=soup.find_all('a')
for i in h:
    print(i.get('href'))
