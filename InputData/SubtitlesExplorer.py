from re import fullmatch


def language_needed():
    languages = []
    language = input("\nEnter the desired language. Enter as (en, ru, ja): ").strip()

    while True:
        if language == "":
            if not languages:
                language = input("\nYou haven't entered any language. You need to enter one: ").strip()
                continue
            break
        
        if not fullmatch(r"[A-Za-z]{2}", language):
            language = input("\nEnter it again in English: ").strip()
            continue
                
        languages.append(language.lower())
        
        language = input("\nEnter more if you want (Press Enter to continue): ").strip()
        

    languages_list = list(dict.fromkeys(languages))

    return languages_list



def view_of_text():
    manually_generated = input("\n1. Manually created transcripts\n2. Generated transcripts\n\nEnter the number: ").strip()

    while True:
        
        if manually_generated in ("1", "2"):
            break

        else:
            manually_generated = input("Enter again: ").strip()
    
    return manually_generated