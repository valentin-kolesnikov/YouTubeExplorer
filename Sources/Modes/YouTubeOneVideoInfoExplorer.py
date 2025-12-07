from Patterns.asyncRYD import ryd

from Patterns.EnteringURL import youtube_id_finder

from Patterns.collectingStats import collect_stats

from SixthFunctions.output import output_info

import asyncio

import os

def launcherInfo(youtube):
    video_id = youtube_id_finder()
    
    statrequest, dict_channels, exc = collect_stats(youtube, video_id)
    if exc:
        os.system('cls')
        return
    
    results = asyncio.run(ryd([video_id]))

    os.system('cls')

    output_info(results, statrequest, dict_channels)

    input("Press Enter to return...")