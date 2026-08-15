from re import search


def get_info():

    NameId = input("Enter the link with UC... or @... to the channel (possible separately): ").strip()

    while True:
        NameId = NameId.strip()
        for_id = search(r"(UC[\w-]{22})", NameId)
        if for_id:
            return for_id.group(1), None
        
        for_handle = search(r"@[\w.-]+", NameId)
        if for_handle:
            return None, for_handle.group(0)

        NameId = input("\nEnter again: ").strip()




def get_answer():
    get_answers = input("\nDo you need to search for videos from the channel?(y/n): ").strip().lower()

    while True:
        if get_answers in ["y", "n"]:
            break

        else:
            get_answers = input("\nEnter again: ").strip().lower()


    return get_answers