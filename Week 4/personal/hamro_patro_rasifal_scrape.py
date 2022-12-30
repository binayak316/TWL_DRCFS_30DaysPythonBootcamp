import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.hamropatro.com/")
page = response.text
soup = BeautifulSoup(page, 'html.parser')
rasifal = soup.find_all('div', class_= "desc")
rasi_list = []

for r in rasifal:
    text = r.getText()
    rasi_list.append(text)


with open("hamropatro.txt",mode='w')as file:
    sn=0
    for rasi in rasi_list:
        file.write(f"{sn} {rasi}")
        file.write("\n") 
        sn +=1