import requests
from bs4 import BeautifulSoup
from flask import Flask


app = Flask(__name__)

@app.route('/')
def loadHomePage():
  return {
    'Homepage' : 'home'
  }

@app.route('/test')
def test():
  response_body = {
    "name": "Kevin",
    "greeting" :"Hello!"
  }
  return response_body

@app.route('/data')
def getCountries():
  # https://brightdata.com/blog/how-tos/web-scraping-with-python
  # Testing out dependencies first


  url = 'https://www.scrapethissite.com/pages/simple/'


  page = requests.get(url)

  # Turns the code into something that you can query
  soup = BeautifulSoup(page.text, 'html.parser')

  soup.find_all('p')[0]

  return soup

  # Check if the soup contains all if the meal times like breakfast lunch and dinner.
  ## I will have to use flask to operate this backend

if __name__ == '__main__':
  app.run(debug=True)
