import pandas as pd

from bs4 import BeautifulSoup

import requests

url = input("Enter a website to extract the URL's from: ")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)
list_rows1 = []
for link in soup.find_all('a'):
    print(link.get('href'))
list_rows1.append(link.text)

df = pd.DataFrame(data={"Product Name":list_rows1})
df.to_csv(r"C:\Users\admin\Desktop\aaa.csv", sep=',',index=False)
df.head(50)