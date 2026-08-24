from ForthFunctions.collecting_info import (
    collect_other_playlists,
    collect_playlist_details,
    collect_your_playlists,
)
from ForthFunctions.output import output_playlists, save_docx
from Patterns.save_history import clear, log, log_error
from Patterns.Search_Engine import search_engine
from PlaylistExplorer_InputData.Videos_of_Playlists import videos_of_playlists


def collection_of_playlists(history, youtube, exc_OAuth2):
    
    print("1. Other's playlists")

    if not exc_OAuth2:
        print("2. Your playlists")

    search_playlist = input("\nChoose the number (Press Enter to return): ").strip()

    while True:
        if search_playlist == "1":

            log(history, "COLLECT_OTHER_PLAYLISTS")
            
            keywords, ageAfter, ageBefore, _, maximum, which_order, _ = search_engine(playlist_enabled=True)
            log(history, "ENTER_FILTERS", keywords=list(keywords), ageAfter=ageAfter, 
                ageBefore=ageBefore, maximum=maximum, which_order=which_order)
            

            playlist_ids, exc = collect_other_playlists(youtube, keywords, ageAfter, ageBefore, maximum, which_order)
            if exc:
                log_error(history, exc, error=True)
                clear()
                return
            
            
            statrequest, exc = collect_playlist_details(youtube, playlist_ids)
            if exc:
                log_error(history, exc, error=True)
                clear()
                return
            
            log(history, "COLLECT_PLAYLISTS", status="SUCCESS")
            clear()

            parsed_playlists = output_playlists(statrequest, keywords)
            log(history, "OUTPUT_PLAYLISTS")

            choice, full_path = save_docx(parsed_playlists, keywords)
            log(history, "SAVE_DOCS", status="SUCCESS" if choice == "y" else "DECLINED", file_path=str(full_path) if choice == "y" else None)

            videos_from_playlist(history, youtube)
            return


        

        elif search_playlist == "2" and not exc_OAuth2:
            log(history, "COLLECT_YOUR_PLAYLISTS")

            statrequest, exc = collect_your_playlists(youtube)
            if exc:
                log_error(history, exc, error=True)
                clear()
                return

            log(history, "COLLECT_PLAYLISTS", status="SUCCESS")
            clear()

            parsed_playlists = output_playlists(statrequest)
            log(history, "OUTPUT_PLAYLISTS")

            choice, full_path = save_docx(parsed_playlists, keywords="Private playlists")
            log(history, "SAVE_DOCS", status="SUCCESS" if choice == "y" else "DECLINED", file_path=str(full_path) if choice == "y" else None)

            videos_from_playlist(history, youtube)
            return
        

        elif search_playlist == "":
            log(history, "BACK_TO_PREVIOUS_MENU")
            clear()
            return

    
        else:
            search_playlist = input("\nEnter again: ").strip()



def videos_from_playlist(history, youtube):
    go_to_another_part = input("\n\nDo you want to analyze the certain playlist? (y/n): ").strip().lower()

    while True:
        if go_to_another_part == "y":
            print("")
            log(history, "COLLECT_VIDEOS_OF_PLAYLISTS")

            videos_of_playlists(history, youtube)

        elif go_to_another_part == "n":
            log(history, "EXIT")
            return
        
        else:
            go_to_another_part = input("Enter again correctly (y/n): ").strip()