from asyncio import run

from InputData.ChannelExplorer import get_answer, get_info
from Patterns.asyncRYD import ryd
from Patterns.check_connection import internet_available
from Patterns.collectingStats import collect_stats
from Patterns.HistoryLogs import HistorySessions
from Patterns.save_history import clear, log, log_error
from Patterns.Search_Engine import search_engine
from ThirdFunctions.collecting_info import (
    collect_channel_info,
    collect_popular_videos,
    search_channel_videos,
)
from ThirdFunctions.output import output_channel_info, save_docx


def launcherChannels(youtube):
    history = HistorySessions("Channel")


    for_id, for_handle = get_info()
    log(history, "ENTER_CHANNEL_LINK", channel_link="https://www.youtube.com/channel/" + for_id if for_id else "https://www.youtube.com/@" + for_handle)


    get_answers = get_answer()
    log(history, "ENTER_ANSWERS", get_answers=get_answers)


    snistics, uploads_videos, exc = collect_channel_info(youtube, for_id, for_handle)
    if exc:
        log_error(history, snistics, exc)
        clear()
        return
    
    
    if get_answers == "y":

        keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension = search_engine(playlist_enabled=False)
        log(history, "ENTER_FILTER_SETTINGS", keywords=keywords, ageAfter=ageAfter, ageBefore=ageBefore,
            duration=duration, maximum=maximum, which_order=which_order, dimension=dimension)
        

        internet_available()
        log(history, "CHECK_INTERNET")


        video_ids, exc = search_channel_videos(youtube, snistics, keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension)
        if exc:
            log_error(history, video_ids, exc)
            clear()
            return
        
        
        result = run(ryd(video_ids))


        statrequests, exc = collect_stats(youtube, video_ids)
        if exc:
            log_error(history, statrequests, exc)
            clear()
            return

        log(history, "COLLECT_CHANNEL_INFO", status="SUCCESS")
        clear()


        parsed_videos = output_channel_info(result, statrequests, get_answers, snistics, keywords)
        log(history, "OUTPUT_CHANNEL_INFO", status="SUCCESS")


        choice, full_path = save_docx(snistics, parsed_videos, keywords)
        log(history, "SAVE_DOCS", status="SUCCESS" if choice == "y" else "DECLINED", file_path=str(full_path) if choice == "y" else None)




    elif get_answers == "n":

        internet_available()
        log(history, "CHECK_INTERNET")


        video_ids, exc = collect_popular_videos(youtube, uploads_videos)
        if exc:
            log_error(history, video_ids, exc)
            clear()
            return
        

        result = run(ryd(video_ids))


        statrequests, exc = collect_stats(youtube, video_ids)
        if exc:
            log_error(history, statrequests, exc)
            clear()
            return
        

        log(history, "COLLECT_CHANNEL_INFO", status="SUCCESS")
        clear()


        parsed_videos = output_channel_info(result, statrequests, get_answers, snistics)
        log(history, "OUTPUT_CHANNEL_INFO", status="SUCCESS")


        choice, full_path = save_docx(snistics, parsed_videos)
        log(history, "SAVE_DOCS", status="SUCCESS" if choice == "y" else "DECLINED", file_path=str(full_path) if choice == "y" else None)


    input("\n\nPress Enter to return...")
    log(history, "EXIT")