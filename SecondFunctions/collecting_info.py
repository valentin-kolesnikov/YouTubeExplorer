from googleapiclient.errors import HttpError

from Patterns.errors import PatternError, WinError, http_error


def collect_searches(youtube, keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension):
    video_ids = []
    next_page_token = None

    while len(video_ids) < maximum:
        remaining_results = maximum - len(video_ids)
        current_max_results = min(remaining_results, 50)

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
                maxResults=current_max_results,
                pageToken=next_page_token
            ).execute()

            
            for item in request["items"]:
                video_ids.append(item["id"]["videoId"])
            
            next_page_token = request.get("nextPageToken")

            if not next_page_token or len(video_ids) >= maximum:
                break

    
        except HttpError as exc:
            error = http_error(exc)
            break
        
        
        except OSError as exc:

            if WinError(exc):
                continue

            error = "OSError occurred"
            break
        
        except Exception as exc:
            error = PatternError().pattern_exception(exc)
            break
    
    return video_ids, error