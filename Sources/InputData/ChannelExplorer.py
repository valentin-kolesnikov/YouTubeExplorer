import re





def get_info():

    NameId = input("\nEnter the link with UC... or @... to the channel (possible separately): ")
    NameId = NameId.strip()

    while True:
        for_id = re.search(r"(UC[\w-]{22})", NameId)
        if for_id:
            return for_id.group(1), None
        
        for_handle = re.search(r"@[\w.-]+", NameId)
        if for_handle:
            return None, for_handle.group(0)

        NameId = input("\nEnter again: ")




def get_answer():
    get_answers = input("\nDo you need to search for videos from the channel?(y/n): ").lower()

    while True:
        if get_answers == "y":
            break

        elif get_answers == "n":
            break

        else:
            get_answers = input("\nEnter again: ").lower()


    return get_answers