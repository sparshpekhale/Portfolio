from os import read
import re
from requests import get
from bs4 import BeautifulSoup

# def get_project(url):
#     # url = 'https://github.com/sparshpekhale/Steganography'

#     soup = BeautifulSoup(get(url).content, 'html.parser')
#     # title = soup.find('strong').find('a').contents[0]
#     title = url.split('/')[-1]

#     readme = soup.find(class_='Box-body px-5 pb-5')
#     # del soup

#     desc_short = readme.find('h2').contents[1]
#     desc_long = readme.find('p').contents[0]
#     image_link = readme.find('img')['src']

#     return title, image_link, desc_short, desc_long

def get_commit(url):
    soup = BeautifulSoup(get(url).content, 'html.parser')
    print(soup.find(class_ = 'Box-header Box-header--blue position-relative').find('include-fragment')['src'].split('/')[-1])