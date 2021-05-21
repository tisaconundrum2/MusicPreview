import json
import requests
import time
import vlc

# Search query goes in the input
print("Please input song query: ", end="")
query = input().replace(" ","+")
# ^ Translates spaces to + to accommodate the URL

# iTunes Search API Format
queryURL = "https://itunes.apple.com/search?term=" + query + "&entity=song"

response = requests.get(queryURL)
response.raise_for_status()

# Consider printing response for debugging
# print(response.text)

songData = json.loads(response.text)

# URLs are only pulled from the first result returned
previewURL = songData['results'][0]['previewUrl']
artworkURL = songData['results'][0]['artworkUrl30']

# Upscale artwork to 1000x1000
artworkURL = artworkURL.replace("30x30bb.jpg","1000x1000bb.jpg")
# No way to display the artwork right now
print(artworkURL)

# Plays the song preview
player = vlc.MediaPlayer(previewURL)
volume = 0
player.audio_set_volume(volume)
count = 0
volumeIncrement = 4
player.play()

# Song previews are 30 seconds long
# 5 seconds added for download time
# time.sleep(35)

# Fade in fade out

while count < 35:
    time.sleep(0.10)
    if count > 2 and count < 5 and volume < 100 - volumeIncrement:
        volume += volumeIncrement
        player.audio_set_volume(volume)
    elif count > 27 and volume > 0:
        volume -= volumeIncrement
        player.audio_set_volume(volume)
    count += 1 * 0.1
