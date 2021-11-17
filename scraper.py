import os
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

def scrape(URL,headers):
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,features='xml')
    return soup

def main():
    for year in range(2004,2014):
        url = f'https://open.alberta.ca/publications/road-ban-orders-{year}'
        soup = scrape(url,headers)
        links = soup.find_all(id='Download')
        download_links = [link['href'] for link in links if link['href'][-4:]=='.pdf']
        for link in download_links:
            r = requests.get(link, allow_redirects=True)
            open('./road ban reports/'+link.split('/')[-1], 'wb').write(r.content)

if __name__ == '__main__':
    main()
