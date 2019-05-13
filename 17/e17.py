import soup as s

url = "https://www.nytimes.com/"

if __name__=="__main__":
    print("Note:\n"
        "\tThe html is now very strange "
            "and there is no sense to check whether this is 100% accurate.\n"
        "\tThe structure and tags will be different in a couple of years anyway.\n\n")

    soup = s.get_soup(url)

    print(* s.get_all_tags(soup,'span'), sep="\n")
    print(* s.get_all_tags(soup,'h2'),   sep="\n")

