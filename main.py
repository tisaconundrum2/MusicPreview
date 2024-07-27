import json
import requests
import time
import os

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

# Download the song preview
preview_response = requests.get(previewURL)
preview_response.raise_for_status()

# Save the preview to a file
with open("song_preview.mp3", "wb") as file:
    file.write(preview_response.content)

print("Song preview downloaded as 'song_preview.mp3'")
