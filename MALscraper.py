import time
import datetime
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

anime_ID=input("Input the ID of the anime you would like to record.")


"""Seasonal anime stats tracker using MAL - via webscraping
"""

start_time = time.time()
# specify the url
quote_page = "https://myanimelist.net/anime/" + anime_ID
# query the website and return the html to the variable ‘page’
page = uReq(quote_page)
page_html = page.read()
page.close()
# parse the html using beautiful soup and store in variable `soup`
page_soup = soup(page_html, "html.parser")

# Name
name = page_soup.h1.text
# Score
score_container = page_soup.findAll("div", {"class": "fl-l score"})
score = score_container[0].text
# Rank
rank_container = page_soup.findAll("span", {"class": "numbers ranked"})
rank = rank_container[0].text.replace('Ranked #', '')
# popularity
pop_container = page_soup.findAll("span", {"class": "numbers popularity"})
pop = pop_container[0].text.replace('Popularity #', '')
# members
mem_container = page_soup.findAll("span", {"class": "numbers members"})
mem = mem_container[0].text.replace('Members ', '')

# csv
new_row = name, quote_page, score.strip(), rank, mem.replace(',', ''), pop, datetime.datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S')
with open('MALscraper.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(new_row)

# print stat info
print(name)
print(quote_page)
print("Score".ljust(14, '-'), score.strip())
print("Rank".ljust(14, '-'), rank)
print("Members".ljust(14, '-'), mem)
print("Popularity".ljust(14, '-'), pop)
print("timestamp".ljust(14, '-'), datetime.datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S'))
print("\n--- %s seconds ---" % (time.time() - start_time))
