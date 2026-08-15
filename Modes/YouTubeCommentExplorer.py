from FirstFunctions.collecting_info import channel_name, collect_comments
from FirstFunctions.output import count_keys, number_comments, save_docx
from InputData.CommentExplorer import youtube_filters
from Patterns.check_connection import internet_available
from Patterns.EnteringURL import youtube_id_finder
from Patterns.HistoryLogs import HistorySessions
from Patterns.save_history import clear, log, log_error


def launcherComments(youtube):
    history = HistorySessions("Comment")

    video_id = youtube_id_finder()
    log(history, "ENTER_VIDEO_LINK", video_link="https://www.youtube.com/watch?v=" + video_id)


    which_order, search_terms = youtube_filters()
    log(history, "ENTER_FILTERS", search_terms=list(search_terms), which_order=which_order)


    internet_available()
    log(history, "CHECK_INTERNET")


    comments, exc = collect_comments(video_id, search_terms, which_order, youtube)
    if exc:
        log_error(history, comments, exc)
        clear()
        return
    

    channel, exc = channel_name(video_id, youtube)
    if exc:
        log_error(history, channel, exc)
        clear()
        return
    
    
    log(history, "COLLECT_COMMENTS", status="SUCCESS")
    clear()
    

    amount_comments, counts = count_keys(comments, search_terms)
    if amount_comments == 0:
        log(history, "NO_COMMENTS")
        clear()
        
        input("\nPress Enter to return...")
        return
    
    
    
    number_comments(comments, channel)
    log(history, "OUTPUT_COMMENTS", status="SUCCESS", amount_comments=amount_comments, counts=counts)


    choice, full_path = save_docx(comments, channel, counts, amount_comments, video_id)
    log(history, "SAVE_DOCS", status="SUCCESS" if choice == "y" else "DECLINED", file_path=str(full_path) if choice == "y" else None)
    

    input("\n\nPress Enter to return...")
    log(history, "EXIT")