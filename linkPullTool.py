#Quick and dirty tool for getting the card names and number from a link

import requests
from bs4 import BeautifulSoup

with open('Total.txt') as f:
    links = f.readlines()

for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find_all('div', class_="plaque")
    title = soup.title.text
    cardscsv = open(title+".txt",'a', encoding="utf-8")

    for element in s:
        key_parts = element.text.split(" - ")
        key_parts[0] = key_parts[0].replace("#", "")
        #print(len(key_parts))
        if (len(key_parts) < 2):
            cardscsv.write(key_parts[0]+ "\n")
        else:
            cardscsv.write(key_parts[0] + "," + key_parts[1] + "\n")
    
    cardscsv.close()