import re

def send_photo(photo_url):
    if hasattr(Api, 'send_photo'):
        Api.send_photo(photo=photo_url)

def process_message(message):
    youtube_patterns = [
        ("https://youtu.be/", "maxresdefault"),
        ("https://youtube.com/watch?v=", "maxresdefault"),
        ("https://m.youtube.com/watch?v=", "maxresdefault"),
        ("https://www.youtube.com/live/", "maxresdefault"),
        ("https://www.youtube.com/shorts/", "hqdefault")
    ]
    
    for pattern, quality in youtube_patterns:
        if pattern in message:
            if pattern in ["https://www.youtube.com/live/", "https://www.youtube.com/shorts/"]:
                split_url = message.split(pattern)[1]
                if split_url:
                    video_id = split_url.split("?")[0]
                    if video_id:
                        photo_url = f"https://i.ytimg.com/vi/{video_id}/{quality}.jpg"
                        send_photo(photo_url)
            else:
                video_id = message.split(pattern)[1].split("&")[0]
                photo_url = f"https://i.ytimg.com/vi/{video_id}/{quality}.jpg"
                send_photo(photo_url)
            return
