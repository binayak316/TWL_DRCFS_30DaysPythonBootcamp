from bs4 import BeautifulSoup
import requests

response = requests.get("https://ekantipur.com/news")
# print(response.text)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
# print(soup.get_text('h2'))
headings_ = soup.find_all('h2')
# author_div = soup.find_all('div', class_ = 'author')
heading_texts = []
authors_list  = []

for h_tag in headings_:
    text = h_tag.getText()
    heading_texts.append(text)
    # print(heading_texts)

author_div =[author.getText() for author in soup.find_all('div', class_ = 'author')]
authors_list.append(author_div)


with open("ekantipur.txt",mode = 'w') as file:
    for news in heading_texts:
        for auth in authors_list:
            file.write(f"Headlines News {news}:- \n by authors: {auth} \n \n")
