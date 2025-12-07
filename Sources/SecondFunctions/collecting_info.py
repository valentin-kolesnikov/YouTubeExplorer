from googleapiclient.errors import HttpError

from Patterns.errors import http_error, WinError





def collect_searches(youtube, keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension):
    try:
        request = youtube.search().list(
            videoDimension=dimension,
            q=keywords,
            regionCode=region,
            publishedBefore=ageBefore,
            order=which_order,
            publishedAfter=ageAfter,
            videoDuration=duration,
            part="snippet",
            type="video",
            maxResults=maximum,
        ).execute()

        video_ids = []
        channel_ids = []

        for item in request["items"]:
            videos = item["id"]["videoId"]
            video_ids.append(videos)

            channels = item["snippet"]["channelId"]
            channel_ids.append(channels)

        return video_ids, channel_ids, False
    
    
    except HttpError as exc:
        
        http_error(exc)
        
        return {}, {}, True
    
    
    except OSError as exc:

        WinError(exc)

        return {}, {}, True


