from Patterns.EnteringURL import youtube_id_finder

from InputData.CommentExplorer import youtube_filters

from FirstFunctions.collecting_info import collect_comments, channel_name

from FirstFunctions.output import count_keys, number_comments

import os






def launcherComments(youtube):
    video_id = youtube_id_finder()

    which_order, search_terms = youtube_filters()

    comments, exc = collect_comments(video_id, search_terms, which_order, youtube)
    if exc:
        os.system('cls')
        return
    
    channel, exc = channel_name(video_id, youtube)
    if exc:
        os.system('cls')
        return
    
    os.system('cls')
    count_keys(comments, search_terms)

    number_comments(comments, channel)

    input("\nPress Enter to return...")