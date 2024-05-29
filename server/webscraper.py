import requests
from bs4 import BeautifulSoup

# https://brightdata.com/blog/how-tos/web-scraping-with-python
# Testing out dependencies first

page = requests.get('https://quotes.toscrape.com')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://quotes.toscrape.com', headers=headers)


soup = BeautifulSoup(page.text, 'html.parser')