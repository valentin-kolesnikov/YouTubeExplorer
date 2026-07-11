from ForthFunctions.collecting_info import collect_other_playlists, collect_playlist_details, collect_your_playlists

from PlaylistExplorer_InputData.Videos_of_Playlists import videos_of_playlists

from ForthFunctions.output import output_playlists

from Patterns.Search_Engine import search_engine

from Patterns.save_history import log, log_error, clear










def collection_of_playlists(history, youtube, exc_OAuth2):
    
    print("1. Other's playlists")

    if not exc_OAuth2:
        print("2. Your playlists")
    print("0. Go back to the previous menu")

    search_playlist = input("\nChoose the number: ").strip()

    while True:
        if search_playlist == "1":

            log(history, "COLLECT_OTHER_PLAYLISTS")
            
            keywords, ageAfter, ageBefore, _, maximum, which_order, _ = search_engine(playlist_enabled=True)
            log(history, "ENTER_FILTERS", keywords=list(keywords), ageAfter=ageAfter, 
                ageBefore=ageBefore, maximum=maximum, which_order=which_order)
            

            playlist_ids, exc = collect_other_playlists(youtube, keywords, ageAfter, ageBefore, maximum, which_order)
            if exc:
                log_error(history, playlist_ids, exc)
                clear()
                return
            
            
            statrequest, exc = collect_playlist_details(youtube, playlist_ids)
            if exc:
                log_error(history, statrequest, exc)
                clear()
                return
            
            log(history, "COLLECT_PLAYLISTS", status="SUCCESS")
            clear()

            output_playlists(statrequest, keywords)
            log(history, "OUTPUT_PLAYLISTS")

            videos_from_playlist(history, youtube)
            return


        

        elif search_playlist == "2" and not exc_OAuth2:
            log(history, "COLLECT_YOUR_PLAYLISTS")

            statrequest, exc = collect_your_playlists(youtube)
            if exc:
                log_error(history, statrequest, exc)
                clear()
                return

            log(history, "COLLECT_PLAYLISTS", status="SUCCESS")
            clear()

            output_playlists(statrequest, keywords)
            log(history, "OUTPUT_PLAYLISTS")

            videos_from_playlist(history, youtube)
            return
        

        elif search_playlist == "0":
            log(history, "BACK_TO_PREVIOUS_MENU")
            clear()
            return

    
        else:
            search_playlist = input("\nEnter again: ").strip()



def videos_from_playlist(history, youtube):
    go_to_another_part = input("\n\nDo you want to analyze the certain playlist? (y/n): ").strip()

    while True:
        if go_to_another_part.lower() == "y":
            print("")
            log(history, "COLLECT_VIDEOS_OF_PLAYLISTS")

            videos_of_playlists(history, youtube)

        elif go_to_another_part.lower() == "n":
            log(history, "EXIT")
            return
        
        else:
            go_to_another_part = input("Enter again correctly (y/n): ").strip()