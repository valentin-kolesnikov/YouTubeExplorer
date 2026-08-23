from FirstFunctions.collecting_info import channel_name, collect_comments
from FirstFunctions.output import count_keys, number_comments, save_docx
from InputData.CommentExplorer import needed_replies, youtube_filters
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
    

    choice_reply = needed_replies()
    log(history, "ENTER_REPLIES", collect_replies=choice_reply)


    internet_available()
    log(history, "CHECK_INTERNET")


    comments, exc = collect_comments(video_id, search_terms, which_order, youtube, choice_reply)
    if exc:
        log_error(history, comments, exc)
        clear()
        return
    

    channel_id, channel_title, exc = channel_name(video_id, youtube)
    if exc:
        log_error(history, channel_id, channel_title, exc)
        clear()
        return
    
    
    log(history, "COLLECT_COMMENTS", status="SUCCESS")
    clear()
    

    amount_comments, amount_replies, total_comments, counts = count_keys(comments, search_terms)
    if amount_comments == 0:
        log(history, "NO_COMMENTS")
        clear()
        
        input("\nPress Enter to return...")
        return
    
    
    
    number = number_comments(comments, channel_id, channel_title)
    log(history, "OUTPUT_COMMENTS", status="SUCCESS", amount_comments=amount_comments, counts=counts)


    choice, full_path = save_docx(comments, channel_id, channel_title, counts, amount_comments, video_id, amount_replies, total_comments, number)
    log(history, "SAVE_DOCS", status="SUCCESS" if choice == "y" else "DECLINED", file_path=str(full_path) if choice == "y" else None)
    

    input("\nPress Enter to return...")
    log(history, "EXIT")