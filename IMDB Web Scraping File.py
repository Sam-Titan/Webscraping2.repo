import requests
from bs4 import BeautifulSoup
import pandas as pd
r = requests.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(r.content, 'html.parser')
data = soup.find_all('h1')
print(data)
