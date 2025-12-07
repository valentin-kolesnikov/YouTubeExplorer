





def youtube_filters():
    search_terms = []
    terms = input("\nEnter the keywords by one (press Enter to continue): ")

    while True:
        if terms == "":
            break

        search_terms.append(terms)
        terms = input("\nMore?: ")

    search_terms = set(search_terms)


    which_order = input("\n1. By relevance\n2. By time\n\nEnter the number: ")

    while True:
        if which_order == "1":
            which_order = "relevance"
            break

        elif which_order == "2":
            which_order = "time"
            break

        else:
            which_order = input("Enter again: ")


    return which_order, search_terms