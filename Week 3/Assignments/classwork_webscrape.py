import requests
import bs4

def send_requests(website_url:str)->str:
    return requests.get(website_url).text

def parse_html_strin(html_str:str)->bs4.BeautifulSoup:
    soup = bs4.BeautifulSoup(html_str,'html.parser')
    return soup

def fetch_rasifal(parsed_html:bs4.BeautifulSoup)->str:
    top_element = parsed_html.find('div',class_="dropdown")
    # print(top_element.text)
    for i, value in enumerate(top_element):
        # print([i,value])
        print(value.text.strip('\n'))
        # print(value.text.strip('\n').split('(')[0])
    

def main():
    website = "https://www.hamropatro.com/"
    html_str: str = send_requests(website)
    parsed_html = parse_html_strin(html_str)
    current_rasifal = fetch_rasifal(parsed_html)
    # print(f"rashifal is {current_rasifal} ")

if __name__ == '__main__':
    main()