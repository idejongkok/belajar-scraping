from bs4 import BeautifulSoup
import urllib.request as request

folder = r'E:\barbuk' + '\\'
URL = 'https://about.google/products/'
response = request.urlopen(URL)
soup = BeautifulSoup(response, 'html.parser')

iconTable = soup.find('ul', {'class':'product-icon-list'})
icons = iconTable.find_all('li')

for barbuk in icons:
    request.urlretrieve(barbuk.img['data-lazy-src'], folder + barbuk.img['alt'] + '.png')
