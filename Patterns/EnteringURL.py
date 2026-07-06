from re import search






def youtube_id_finder():
    url = input("Enter the video URL: ")

    while True:
        pattern = r"(?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/|shorts/))?([0-9A-Za-z_-]{11})"
        match = search(pattern, url)

        if match:
            return match.group(1)
        
        else:
            url = input("\nEnter the URL again correctly: ")