import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"

def print_all_tags(tag_name):
    for tag in soup.find_all(tag_name):
        tag_s = tag.string
        if tag_s: print(tag_s)


if __name__=="__main__":
    print("Note:\n"
        "\tThe html is now very strange "
            "and there is no sense to check whether this is 100% accurate.\n"
        "\tThe structure and tags will be different in a couple of years anyway.\n\n")

    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "lxml")

    print_all_tags('span')
    print_all_tags('h2')

