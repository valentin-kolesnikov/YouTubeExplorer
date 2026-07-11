from datetime import datetime



def output_playlists(statrequest, keywords=None):
    if keywords:
        print(f"Your request: {keywords}")

    number = 0
    for item in statrequest["items"]:
        title = item["snippet"]["title"]
        playlist_id = item["id"]
        published_at = item["snippet"]["publishedAt"]
        dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        formatted_date = dt.strftime("%d.%m.%Y %H:%M:%S")

        status = item["status"]["privacyStatus"]
        itemCount = item["contentDetails"]["itemCount"]

        channelName = item["snippet"]["channelTitle"]
        channelId = item["snippet"]["channelId"]

        number += 1

        print(
            f"\n{number}."
            f"{title}\n"
            f"Playlist URL: https://www.youtube.com/playlist?list={playlist_id}\n"
            f"Privacy status: {status}; Videos: {itemCount}\n"
            f"{formatted_date}\n"
            f"{channelName}\n"
            f"Channel URL: https://www.youtube.com/channel/{channelId}")

        # If there are a lot of information, I need to add a feature to create DOCX