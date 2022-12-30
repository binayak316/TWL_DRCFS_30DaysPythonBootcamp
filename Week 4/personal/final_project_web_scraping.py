# scraper to scrape products detials from hamrobazzar app

import requests
from bs4 import BeautifulSoup

url = "https://ekantipur.com/news"

def website_scraper(url:str)-> list:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tag = soup.find_all('h2')
    # name = soup.select(".heading") by using css selector
    a_tag = tag
    # print(a_tag)
    for a in a_tag:
        text = a.text
        print(["*** "+ text + " ***"])


    # print(division) 
website_scraper(url)