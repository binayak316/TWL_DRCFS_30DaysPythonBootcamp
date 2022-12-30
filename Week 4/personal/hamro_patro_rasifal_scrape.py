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
    for rasi in rasi_list:
        file.write(f"{rasi}")
    # file.write(f"{rasi_list}")