from datetime import datetime


def output_info(results, statrequest, dict_channel):

    for item in statrequest["items"]:
        title = item["snippet"]["title"]
        video_id = item["id"]
        published_at = item["snippet"]["publishedAt"]
        dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        formatted_date = dt.strftime("%d.%m.%Y %H:%M:%S")

        likes = results.get(video_id, {}).get("likes", "No")
        dislikes = results.get(video_id, {}).get("dislikes", "No")
        views = results.get(video_id, {}).get("viewCount", "No")
        comments = item["statistics"].get("commentCount", "No")



        
        print(
            f"Title: {title}\n"
            f"Video Link: https://www.youtube.com/watch?v={video_id}\n"
            f"{views} views; {likes} likes; {dislikes} dislikes; {comments} comments\n"
            f"Description of the video:\n=================================\n{dict_channel["description"]}\n=================================\n"
            f"Date: {formatted_date}\n"
            f"Channel: {dict_channel.get('Name', 'N/A')}\n"
            f"Channel Link: https://www.youtube.com/channel/{dict_channel["Id"]}\n")