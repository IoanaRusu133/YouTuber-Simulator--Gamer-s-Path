import requests
from bs4 import BeautifulSoup

def scrape_games():
    url = 'https://store.steampowered.com/search/?filter=topsellers'
    games_dict = {}

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    games = soup.find_all('div', class_ ='responsive_search_name_combined')

    n = 0
    for g in games:
        if n<20:
            title = g.find('span', class_ = 'title').text
            price_raw = g.find('div', class_ = 'discount_final_price').text
            price = ''
            if 'Free' in price_raw:
                price = 0.00
            else:
                for p in price_raw:
                    if p in ('0123456789.,'):
                        price += p
                price = price.replace(',', '.')
            price = float(price)
            games_dict[title] = [price]
            n += 1

    return games_dict


games_dict = scrape_games()