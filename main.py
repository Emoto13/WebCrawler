import requests
from bs4 import BeautifulSoup
import validators


def main():
    res = requests.get('https://hackbulgaria.com')
    soup = BeautifulSoup(res.content, 'html.parser')
    hyperlinks = soup.find_all('a')
    
    for hyperlink in hyperlinks:
        link = hyperlink.get('href')
        if link is not None and validators.url(link):
            print(link)


if __name__ == '__main__':
    main()
