# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:26:56 2018

@author: iamsmnt
"""

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd





url = 'https://www.flipkart.com/mens-footwear/casual-shoes/pr?sid=osp,cil,e1f&otracker=nmenu_sub_Men_0_Casual%20Shoes'

html = urlopen(url)
""" So now our page is downloaded and saved in the variable r
Now we need to parse the HTML of that page to retrieve the information. For that we will use BeautifulSoup4
"""

soup = BeautifulSoup(html,'lxml')


title = soup.title

print(title)

text = soup.get_text()

#the data structure to save the values
shoes_ = []
ratings_ =  []
prices_ = []
discounts_ = []
d_price = []

#class and attribute search of html tags using BeautifulSoup
all_shoes = soup.find_all("a",attrs = {"class":"_2cLu-l"})
all_ratings = soup.find_all("div",attrs = {"class":"hGSR34 _2beYZw"})
all_prices = soup.find_all("div", attrs = {"class":"_3auQ3N"})
all_discounts = soup.find_all("div",attrs = {"class":"VGWI6T"})
all_dp = soup.find_all("div",attrs = {"class":"_1vC4OE"})


l=0
for shoes in all_shoes:
    l += 1
    if l < 41: #setting the limit to scrape items in the first page
        shoes_.append(shoes.get_text())

i = 0  
for ratings in all_ratings:
    i += 1
    if i < 41:
        ratings_.append(ratings.get_text()) 
j = 0    
for prices in all_prices:
    j += 1
    if j < 41:
        prices_.append(prices.get_text())
k = 0   
for discounts in all_discounts:
    k += 1
    if k < 41:
        discounts_.append(discounts.get_text())

m = 0
for d_prices in all_dp:
    m += 1
    if m < 41:
        d_price.append(d_prices.get_text())

val = [shoes_,ratings_,prices_,discounts_]

labels = ['shoes']
products_df = pd.DataFrame({'shoes':shoes_,'ratings':ratings_,'prices':prices_,'discounts':discounts_,'discount price':d_price})

products_df.to_csv('flipkart_shoes.csv',index = True) # saving the scraped items into a csv.file
