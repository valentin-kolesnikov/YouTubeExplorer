from InputData.VideoExplorer import searching_for_videos

from SecondFunctions.collecting_info import collect_searches

from Patterns.collectingStats import collect_stats

from SecondFunctions.output import output_videos

from Patterns.asyncRYD import ryd

import os

import asyncio







def launcherVideos(youtube):
    keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension = searching_for_videos()
    
    video_ids, exc = collect_searches(youtube, keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension)
    if exc:
        os.system('cls')
        return

    results = asyncio.run(ryd(video_ids))

    statrequest, exc = collect_stats(youtube, video_ids)
    if exc:
        os.system('cls')
        return
    
    os.system('cls')

    output_videos(results, statrequest)

    input("Press Enter to return...")