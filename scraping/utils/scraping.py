import requests
from bs4 import BeautifulSoup
from utils.file_operations import save_data

def scrape_data():
    page = 1

    for request in range(24):
        response = requests.get('https://data.un.org/Data.aspx?d=POP&f=tableCode%3a240%3bcountryCode%3a616%3brefYear%3a2011%2c2012%2c2013%2c2014%2c2015%2c2016%2c2017%2c2018%2c2019%2c2020%2c2021'
                                f'&c=2,3,10,12,17,18&s=_countryEnglishNameOrderBy:asc,refYear:desc,areaCode:asc&v={page}')

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('div', class_='DataContainer')
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')
            cell_texts = [cell.get_text(strip=True) for cell in cells]
            save_data(f"{';'.join(cell_texts)}\n")

        page += 1
