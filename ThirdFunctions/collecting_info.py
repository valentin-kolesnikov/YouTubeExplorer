from googleapiclient.errors import HttpError

from Patterns.errors import PatternError, http_error, WinError

from datetime import datetime






def collect_channel_info(youtube, for_id, for_handle):
    while True:
        try:
            request = youtube.channels().list(
                part="snippet,statistics,contentDetails",
                forHandle=for_handle,
                id=for_id
            ).execute()
            
            if "items" in request and request["items"]:
                channel_id = request["items"][0]["id"]
            else:
                raise ValueError
            
            snippet = request["items"][0]["snippet"]
            statistics = request["items"][0]["statistics"]

            chpublished_at = snippet.get("publishedAt")
            dt = datetime.fromisoformat(chpublished_at.replace("Z", "+00:00"))
            chformatted_date = dt.strftime("%d.%m.%Y")
            

            snistics = {
                "title": snippet.get("title"),
                "channelId": channel_id,
                "description": snippet.get("description"),
                "publishedAt": chformatted_date,
                "customUrl": snippet.get("customUrl", "N/A"),  
                "viewCount": statistics.get("viewCount"),
                "subscriberCount": statistics.get("subscriberCount"),
                "videoCount": statistics.get("videoCount")
            }

            uploads_videos = request["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
            

            return snistics, uploads_videos, False
        

        except HttpError as exc:

            issue = http_error(exc)

            return issue, {}, True
        
        
        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", {}, True
        
        
        except Exception:

            if ValueError:
                issue = "The channel is not found."

            else:
                issue = "Unknown problem."

            print(f"\n{issue}")

            input("\nPress Enter to return...")

            return issue, {}, True
    

    
    
    
def search_channel_videos(youtube, snistics, keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension):
    while True:
        try:
            video_ids = []
            next_page_token = None

            while True:
                remaining_results = maximum - len(video_ids)

                if remaining_results <= 0:
                    break

                current_max_results = min(remaining_results, 50)
                
                video_collection = youtube.search().list(
                    part="snippet",
                    channelId=snistics['channelId'],
                    q=keywords,
                    type="video",
                    maxResults=current_max_results,
                    videoDimension=dimension,
                    publishedBefore=ageBefore,
                    order=which_order,
                    publishedAfter=ageAfter,
                    videoDuration=duration,
                    pageToken=next_page_token
                ).execute()

                for item in video_collection["items"]:
                    video_ids.append(item["id"]["videoId"])

                next_page_token = video_collection.get("nextPageToken")

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

    

def collect_popular_videos(youtube, uploads_videos):
    while True:
        try:
            video_ids = []

            collection = youtube.playlistItems().list(
                part="contentDetails",
                playlistId=uploads_videos,
                maxResults=4
            ).execute()

            for item in collection["items"]:
                video_ids.append(item["contentDetails"]["videoId"])


            return video_ids, False


        except HttpError as exc:

            issue = http_error(exc)

            return issue, True
        

        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception:
            return PatternError().pattern_exception(), True