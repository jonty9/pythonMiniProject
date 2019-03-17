from urllib.request import urlopen
from bs4 import BeautifulSoup


def crypto():
    link = 'https://coinmarketcap.com/'
    htmlPage = urlopen(link)

    soupPage = BeautifulSoup(htmlPage, 'html.parser')

    coinName = soupPage.findAll('a', attrs={'class': 'currency-name-container'})
    coinMarketCap = soupPage.findAll('td', attrs={'class': 'market-cap'})
    coinPrice = soupPage.findAll('a', attrs={'class': 'price'})
    coinVolume = soupPage.findAll('a', attrs={'class': 'volume'})
    coinChange = soupPage.findAll('td', attrs={'class': 'percent-change'})
    for i in range(0, 10):
        coin = str(i + 1) + '. ' + coinName[i].text + coinMarketCap[i].text + coinPrice[i].text + coinVolume[
            i].text + '\nPercentage change(24h) ' + coinChange[i].text + '\n'
        t.insert(END, coin)
