import requests
from bs4 import BeautifulSoup as bsp
req=requests.get('https://www.python.org/')
soup=bsp(req.content,'html.parser')
t=soup.a
print(t.prettify())
