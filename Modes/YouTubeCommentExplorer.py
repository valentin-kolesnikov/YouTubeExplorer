from Patterns.EnteringURL import youtube_id_finder

from InputData.CommentExplorer import youtube_filters

from FirstFunctions.collecting_info import collect_comments, channel_name

from FirstFunctions.output import count_keys, number_comments, save_docx

from Patterns.check_connection import internet_available

from Patterns.HistoryLogs import HistorySessions




def launcherComments(youtube):
    history = HistorySessions("Comment")

    video_id = youtube_id_finder()
    history.add_session("ENTER_VIDEO_ID", video_link="https://www.youtube.com/watch?v=" + video_id)
    history.save()


    which_order, search_terms = youtube_filters()
    history.add_session("ENTER_FILTERS", search_terms=list(search_terms), which_order=which_order)
    history.save()

    internet_available()
    history.add_session("CHECK_INTERNET")
    history.save()


    comments, exc = collect_comments(video_id, search_terms, which_order, youtube)
    if exc:
        history.add_session("ERROR", reason=comments, error=str(exc))
        history.save()

        print("\033[H\033[J", end="")
        return
    

    channel, exc = channel_name(video_id, youtube)
    if exc:
        history.add_session("ERROR", reason=channel, error=str(exc))
        history.save()

        print("\033[H\033[J", end="")
        return
    
    history.add_session("COLLECT_COMMENTS", status="SUCCESS")
    history.save()
    
    print("\033[H\033[J", end="")



    amount_comments, counts = count_keys(comments, search_terms)
    if amount_comments == 0:
        history.add_session("NO_COMMENTS")
        history.save()
        
        input("\nPress Enter to return...")
        return
    
    
    
    number_comments(comments, channel)
    history.add_session("OUTPUT_COMMENTS", status="SUCCESS", amount_comments=amount_comments, counts=counts)
    history.save()



    choice, full_path = save_docx(comments, channel, counts, amount_comments, video_id)

    if choice == "y":
        history.add_session("SAVE_DOCS", status="SUCCESS", file_path=str(full_path))
    elif choice == "n":
        history.add_session("SAVE_DOCS", status="DECLINED")
    
    history.save()

    input("\n\nPress Enter to return...")