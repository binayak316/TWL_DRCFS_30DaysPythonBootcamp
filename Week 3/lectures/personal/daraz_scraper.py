#go to daraz site for a specific product
# fetch it's current price
# write that price to a file every 60 seconds
# reqyest the daraz product page using requests module
# parse the html string using bs4
# find the element that contains the price
# conver the price into int
# write the price in file

import bs4
import requests
from datetime import datetime


def request_site(url:str)->str:
    return requests.get(url, timeout=100).text

def parse_html(unparsed_html:str)->bs4.BeautifulSoup:
    return bs4.BeautifulSoup(unparsed_html,'html.parser')

def get_price_from_soup(soup:bs4.BeautifulSoup)->str:
    price_element = soup.find('span',class_="price-wrapper")
    nepali_price = price_element.span.string #span vitra ko arko span bata .string bata data nikaleko
    return nepali_price

def write_price_to_file(price:str,filename:str)->None:
    with open(filename,mode='a',encoding='utf-8') as file:
        file.write(price)
        file.write('\n')

def main():
    website_url = "https://www.sastodeal.com/baltra-sensible-plus-electric-2-burner-infrared-cooker-bic-126-supply-baltra-09.html"
    file_path = "data.txt"
    html_str = request_site(website_url)
    soup = parse_html(html_str)
    price = get_price_from_soup(soup)
    write_price_to_file(price, file_path)


if __name__ == '__main__':
    main()