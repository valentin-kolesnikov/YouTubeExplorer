from InputData.ChannelExplorer import get_info, get_answer

from ThirdFunctions.collecting_info import collect_channel_info, search_channel_videos, collect_channel_stats_videos, collect_popular_videos, collect_statistics

from ThirdFunctions.output import output_channel_info

from Patterns.Search_Engine import search_engine

from Patterns.asyncRYD import ryd

import os

import asyncio







def launcherChannels(youtube):
    for_id, for_handle = get_info()

    get_answers = get_answer()

    snistics, uploads_videos, exc = collect_channel_info(youtube, for_id, for_handle)
    if exc:
        os.system('cls')
        return
    
    if get_answers == "y":

        keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension = search_engine()

        video_Ids, exc = search_channel_videos(youtube, snistics, keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension)
        if exc:
            os.system('cls')
            return
        
        result = asyncio.run(ryd(video_Ids))

        statrequests, exc = collect_channel_stats_videos(youtube, video_Ids)
        if exc:
            os.system('cls')
            return

        output_channel_info(result, statrequests, get_answers, snistics)

    elif get_answers == "n":
        videoIds, exc = collect_popular_videos(youtube, uploads_videos)
        if exc:
            os.system('cls')
            return

        result = asyncio.run(ryd(videoIds))

        statrequests, exc = collect_statistics(youtube, videoIds)
        if exc:
            os.system('cls')
            return
        
        output_channel_info(result, statrequests, get_answers, snistics)

    input("\nPress Enter to return...")