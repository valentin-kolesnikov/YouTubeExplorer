from googleapiclient.errors import HttpError

from Patterns.errors import PatternError, WinError, http_error


def channel_name(video_id, youtube):
    while True:
        try:
            name = youtube.videos().list(
                part="snippet",
                id=video_id
            ).execute()

            items = name.get("items", [])

            return items[0]["snippet"]["channelId"], items[0]["snippet"]["channelTitle"], False

            

        except HttpError as exc:
            
            issue = http_error(exc)

            return issue, True
        

        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception as exc:
            return PatternError().pattern_exception(exc), True
    


    
def collect_comments(video_id, search_terms, which_order, youtube, choice_reply):
    comments = []
    next_page_token = None

    search_terms_lower = [term.lower() for term in search_terms]

    while True:
        try:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                textFormat="plainText",
                order=which_order,
                pageToken=next_page_token
            ).execute()

            for item in request["items"]:

                top_comment = item["snippet"]["topLevelComment"]
                snippet = top_comment["snippet"]

                comment_id = item["snippet"]["topLevelComment"]["id"]
                comment_text = snippet["textDisplay"]

                if (not search_terms_lower 
                    or any(
                        term in comment_text.lower() 
                        for term in search_terms_lower
                    )
                ):
                    comments.append({
                        "id": comment_id,
                        "text": comment_text,
                        "author": snippet["authorDisplayName"],
                        "viewerRating": snippet["viewerRating"],
                        "likeCount": snippet["likeCount"],
                        "published_at": snippet["publishedAt"],
                        "updated_at": snippet["updatedAt"],
                        "replies": []
                    })

            next_page_token = request.get("nextPageToken")

            if not next_page_token:
                break
        
        
        except HttpError as exc:
            return http_error(exc), True
        
        
        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception as exc:
            return PatternError().pattern_exception(exc), True
        

    for comment in comments:
                    
        if choice_reply:
            replies, exc = collect_replies(youtube, comment["id"])

            if exc:
                return replies, True

            
            comment["replies"] = replies    


            
    return comments, False





def collect_replies(youtube, comment_id):
    replies = []
    next_page_token = None

    while True:
        try:
            request_replies = youtube.comments().list(
                part="snippet",
                parentId=comment_id,
                maxResults=100,
                textFormat="plainText",
                pageToken=next_page_token
            ).execute()

            for item in request_replies["items"]:
                reply_snippet = item["snippet"]

                replies.append({
                    "id": item["id"],
                    "text": reply_snippet["textDisplay"],
                    "author": reply_snippet["authorDisplayName"],
                    "viewerRating": reply_snippet["viewerRating"],
                    "likeCount": reply_snippet["likeCount"],
                    "published_at": reply_snippet["publishedAt"],
                    "updated_at": reply_snippet["updatedAt"]
                })

            next_page_token = request_replies.get("nextPageToken")

            if not next_page_token:
                return replies, False

        except HttpError as exc:
            return http_error(exc), True
                
                
        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception as exc:
            return PatternError().pattern_exception(exc), True