#imports
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Site to scrap from
link = 'https://coinmarketcap.com/'

#Download Page
htmlPage = urlopen(link)

#Parse HTML into BeautifulSoup
soupPage = BeautifulSoup(htmlPage, 'html.parser')

#Find Currency Details
coinName = soupPage.findAll('a', attrs={'class' : 'currency-name-container'})
coinMarketCap = soupPage.findAll('td', attrs={'class' : 'market-cap'})
coinPrice = soupPage.findAll('a', attrs={'class' : 'price'})
coinVolume = soupPage.findAll('a' , attrs={'class' : 'volume'})
coinChange = soupPage.findAll('td' , attrs={'class' : 'percent-change'})

#Format and print details
c = int(input('How many currencies would you like? '))
for i in range(0, c):
    coin = str(i+1) + '. ' + coinName[i].text +  coinMarketCap[i].text + coinPrice[i].text + coinVolume[i].text + '\nPercentage change(24h) ' + coinChange[i].text
    print(coin)


 # #Market cap
# coinMarketCap = soupPage.find('td', attrs={'class' : 'market-cap'})
# #print(coinMarketCap)
# Marketcap = coinMarketCap.text
# print(Marketcap)
#
# #Price
# coinPrice = soupPage.find('a', attrs={'class' : 'price'})
# #print(coinPrice)
# price = coinPrice.text
# print(price)
#
# #Volume
# coinVolume = soupPage.find('a' , attrs={'class' : 'volume'})
# #print(coinVolume)
# volume = coinVolume.text
# print(volume)