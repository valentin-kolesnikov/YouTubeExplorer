from Patterns.fileCalendar import age_calendar


def search_engine(playlist_enabled=False):
    keywords = input("\nEnter a request on YouTube: ").strip()

    while True:
        if not keywords:
            keywords = input("\nEnter again: ").strip()

        else:
            break


    filterQ = input("\nDo you need to filter resources?(y/n): ").strip().lower()
    while True:
        if filterQ == "y":

            sort = input("\nDo you need to sort by something?(y/n): ").strip().lower()
            if sort == "y":
                which_orderDict = {
                    "1": "relevance",
                    "2": "date",
                    "3": "viewCount",
                    "4": "rating",
                    "5": "title",
                    "6": "help"
                }

                which_order = input("\n1. relevance\n2. date\n3. viewCount\n4. rating\n5. title\n6. help\n\nEnter the number: ").strip()
                while True:
                    if which_order == "6":

                        which_order = input("" \
                        "\n1. relevance - default" \
                        "\n2. date - sort by upload date" \
                        "\n3. viewCount - sort from highest to lowest number of views" \
                        "\n4. rating - sort from highest to lowest rating" \
                        "\n5. title - sort alphabetically by title\n" \
                        "\nEnter the number again: ").strip()

                    elif which_order in which_orderDict:
                        which_order = which_orderDict[which_order]
                        break

                    else:
                        which_order = input("\nEnter again: ").strip()
                        
                if not playlist_enabled:
                    dimensionDict = {
                        "1": "2d",
                        "2": "3d",
                        "3": "any"
                    }
                    dimension = input("\nWhat dimension do you need?" \
                    "\n1. 2d" \
                    "\n2. 3d" \
                    "\n3. Any" \
                    "\n\nEnter the number: ").strip()

                    while True:
                        if dimension in dimensionDict:
                            dimension = dimensionDict[dimension]
                            break

                        else:
                            dimension = input("\nEnter again: ").strip()
            else:
                which_order = "relevance"
                dimension = "any"

            dateBefore = input("\nDo you need resources before some time?(y/n): ").strip().lower()
            while True: 
                if dateBefore == "y":
                    yearB, monthB, dayB = age_calendar(dateBefore=True)

                    ageBefore = (f"{yearB}-{monthB}-{dayB}T00:00:00Z")

                    break

                elif dateBefore == "n":
                    ageBefore = None
                    break
                
                else:
                    dateBefore = input("\nEnter again: ").strip().lower()


            dateAfter = input("\nDo you need resources after some time?(y/n): ").strip().lower()
            while True:

                if dateAfter == "y":
                    yearA, monthA, dayA = age_calendar(dateAfter=True)
                    
                    ageAfter = (f"{yearA}-{monthA}-{dayA}T00:00:00Z")

                    break

                elif dateAfter == "n":
                    ageAfter = None
                    break

                else:
                    dateAfter = input("\nEnter again: ").strip().lower()
            

            if not playlist_enabled:
                durationQ = input("\nDo you need a duration of video?(y/n): ").strip().lower()
                
                while True:

                    if durationQ == "y":
                        
                        durationDict = {
                        "1": "short",
                        "2": "medium",
                        "3": "long"
                        }
                        
                        duration = input("\n1. Short - less 4 minutes" \
                        "\n2. Medium - from 4 to 20 minutes" \
                        "\n3. Long - from 20 minutes" \
                        "\n\nEnter the number: ").strip()

                        while True:
                            if duration in durationDict:
                                duration = durationDict[duration]
                                break

                            else:
                                duration = input("\nEnter again: ").strip()

                    elif durationQ == "n":
                        duration = "any"
                        break

                    else:
                        durationQ = input("\nEnter again: ").strip().lower()

                    break

            break    
        
        elif filterQ == "n":
            which_order = "relevance"
            dimension = "any"
            ageBefore = None
            ageAfter = None
            duration = "any"
            break

        else:
            filterQ = input("\nEnter again: ").strip().lower()


    maximum = input("\nHow much do you want to receive resources?: ").strip()

    while True:
        if maximum.isdigit() and int(maximum) > 0:
            break

        maximum = input("\nEnter the number greater than 0: ").strip()


    return keywords, ageAfter, ageBefore, duration, int(maximum), which_order, dimension