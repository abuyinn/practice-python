import requests
from bs4 import BeautifulSoup

def get_all_tags(_soup, _tag_name):
    tags = []
    for tag in _soup.find_all(_tag_name):
        tag_str = tag.string
        if tag_str: tags.append(tag_str)
    return tags

def get_soup(_url):
    r = requests.get(_url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "lxml")
    return soup

