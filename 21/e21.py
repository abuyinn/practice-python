#!/use/bin/env python3

import soup as s

url = "https://www.nytimes.com/"
default_name = "article.txt"


def check_filename(_filename,_default):
    if _filename=='':    return _default
    if '/' in _filename: return _default
    return _filename


if __name__=="__main__":
    filename = check_filename(input("Filename ["+default_name+"]: "),default_name)
    soup = s.get_soup(url)
    articles_list = (s.get_all_tags(soup,'span') +
                     s.get_all_tags(soup,'h2')   + ['\n'])

    with open(filename,'w') as f:
        f.write('\n'.join(articles_list))

