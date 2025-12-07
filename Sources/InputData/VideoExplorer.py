from Patterns.Search_Engine import search_engine





def searching_for_videos():
    region = input("\nWhat region would you like? (Enter as US, RU, UK, etc): ").upper()
    while True:
        if len(region) == 2 and region.isalpha():
            break

        else:
            region = input("\nEnter again: ").upper()



    keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension = search_engine()


    return keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension