import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

if __name__=="__main__":
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "lxml")

    # usefull tags
    h1   = soup.find('h1')
    span = soup.find_all('span')
    p    = soup.find_all('p')


    #########
    # title
    print(h1.string,"\n")

    ##########
    # header
    # ...is tough, it looks different sometimes

    # 1st looks
    x = soup.find(class_="content-header__row content-header__dek")
    if x: print(x.string)
    
    # 2nd looks
    for e in span:
        if e.string and e.has_attr('data-reactid') and e['data-reactid']=="177":
            print(e.string)

    # separation
    print()

    #################
    # next sections
    # ...are just p without class
    for txt in p:
        t = txt.string
        if t and not txt.has_attr('class'):
            print("\n",t)

