from tkinter import *

from urllib.request import urlopen
from bs4 import BeautifulSoup

def crypto():
    t.delete('1.0', END)
    saveButton.config(text="Save Data")
    n = int(inputBox.get())
    link = 'https://coinmarketcap.com/'
    htmlPage = urlopen(link)

    soupPage = BeautifulSoup(htmlPage, 'html.parser')

    coinName = soupPage.findAll('a', attrs={'class': 'currency-name-container'})
    coinMarketCap = soupPage.findAll('td', attrs={'class': 'market-cap'})
    coinPrice = soupPage.findAll('a', attrs={'class': 'price'})
    coinVolume = soupPage.findAll('a', attrs={'class': 'volume'})
    coinChange = soupPage.findAll('td', attrs={'class': 'percent-change'})
    for i in range(0, n):
        coin = str(i + 1) + '. ' + coinName[i].text + '\nMarket Cap ' + coinMarketCap[i].text + 'Coin Price ' + coinPrice[i].text + '\nCoin Volume ' + coinVolume[
            i].text + '\nPercentage change(24h) ' + coinChange[i].text + '\n'
        t.insert(END, coin)
    saveButton.config(state= NORMAL)

def save():
    data = t.get("1.0", END)
    fileName = fileNameBox.get()
    f = open(fileName + '.txt', "w+")
    f.write(data)
    f.close
    saveButton.config(text="Done!")
    saveButton.config(state = DISABLED)

window = Tk()
window.title("Crypto Web Scrapper")
window.minsize(500,500)
window.geometry("800x600")
inputBox = Entry(window)
subButton = Button(window, text= 'Search!',activebackground = 'blue', command = crypto)
inputBox.pack()
subButton.pack()
t= Text(window, height=30, width=50)
t.pack()
fileNameBox = Entry(window)
fileNameBox.pack()
saveButton = Button(window, text= 'Save Data',state= DISABLED, command = save)
saveButton.pack()

window.mainloop()
