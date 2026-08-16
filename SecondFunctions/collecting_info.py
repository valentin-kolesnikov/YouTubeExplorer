from googleapiclient.errors import HttpError

from Patterns.errors import PatternError, WinError, http_error


def collect_searches(youtube, keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension):
    while True:
        try:
            video_ids = []
            next_page_token = None

            while True:
                remaining_results = maximum - len(video_ids)

                if remaining_results <= 0:
                    break

                current_max_results = min(remaining_results, 50)

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
                    maxResults=current_max_results,
                    pageToken=next_page_token
                ).execute()

                
                for item in request["items"]:
                    video_ids.append(item["id"]["videoId"])
                
                next_page_token = request.get("nextPageToken")

                if not next_page_token or len(video_ids) >= maximum:
                    break

            return video_ids, False
        
        
        except HttpError as exc:
            
            issue = http_error(exc)
            
            return issue, True
        
        
        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception as exc:
            return PatternError().pattern_exception(exc), True