import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list =[]
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,features="html.parser")
    for post_text in soup.findAll('a',{'class' : 'result-title hdrlnk'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):

    clean_up_list = []
    for word in word_list:
        print(word)

start("https://seattle.craigslist.org/search/jjj")