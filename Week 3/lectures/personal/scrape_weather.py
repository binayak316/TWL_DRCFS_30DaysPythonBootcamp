# goto a weather website 
# get the current temperature and weather for your local city
# print the current temperature and weather

# hit the website using requests modules
# parse the html returned by requests module using bs4 module
# fetch the current temperature and weather using the parsed html
# print it

import requests
import bs4

def send_request(website_url:str)->str:#return type diyeko ra :str va vane teslai type hinted vaninxa 
    return requests.get(website_url).text #raw string chaiyexa vannale html form ma so .text


def parse_html_string(html_str:str)->bs4.BeautifulSoup:
    soup = bs4.BeautifulSoup(html_str, 'html.parser')
    return soup


def fetch_current_temperature(parsed_html:bs4.BeautifulSoup)->str:
    top_element = parsed_html.find(id="top")
    date_element=top_element.find('div',class_="date")
    current_date = date_element.span.string.removeprefix('\n')
    # print(current_date)
    return current_date
    
def main(): #this call send requests
    website = "https://www.hamropatro.com/"
    html_str: str = send_request(website) #:str gareko type hinted ho
    parsed_html = parse_html_string(html_str)
    # print(parsed_html)
    current_date = fetch_current_temperature(parsed_html)
    print(f"The current date is {current_date}.")


if __name__ == '__main__':
    main()

