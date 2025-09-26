from yt_dlp import YoutubeDL
import json

downloader = YoutubeDL({"skip_download": True,
                        "writeautomaticsub": True})

data = downloader.extract_info("https://www.youtube.com/watch?v=OCIVI6M48KM")

with open("data.json", "w") as f:
    json.dump(data, f)
