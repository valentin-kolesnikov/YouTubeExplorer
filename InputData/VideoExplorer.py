from Patterns.Search_Engine import search_engine

from re import fullmatch





def searching_for_videos():
    region = input("What region would you like? (Enter as US, RU, UK, etc): ").strip().upper()
    while True:
        if not fullmatch(r"[A-Za-z]{2}", region):
            region = input("\nEnter it again in English: ").strip().upper()
        else:
            break

        


    keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension = search_engine()


    return keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension