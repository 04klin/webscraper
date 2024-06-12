import requests
from bs4 import BeautifulSoup
from flask import Flask


app = Flask(__name__)

@app.route('/')
def loadHomePage():
  return {
    'Homepage' : 'home'
  }

@app.route('/data')
def getCountries():
  # https://brightdata.com/blog/how-tos/web-scraping-with-python
  # Testing out dependencies first


  url = 'https://www.scrapethissite.com/pages/simple/'


  page = requests.get(url)

  # Turns the code into something that you can query
  soup = BeautifulSoup(page.text, 'html.parser')

  # Gathers total area and number of countries
  allAreas = soup.find_all(class_= 'country-area')
  counter = 0
  sumLand = 0
  for a in allAreas:
    counter += 1
    sumLand += float(a.text)
  sumLand = "{:,}".format(sumLand)
  # Gathers total population
  totalPop = soup.find_all(class_= 'country-population')

  sumPop = 0
  for a in totalPop:
    sumPop += int(a.text)
  sumPop = "{:,}".format(sumPop)

  # JSON return file
  ret = {
    'numOfCountries' : counter,
    'landSum' : sumLand,
    'popSum' : sumPop
  }

  return ret

  # Check if the soup contains all if the meal times like breakfast lunch and dinner.
  ## I will have to use flask to operate this backend



if __name__ == '__main__':
  app.run(debug=True)
