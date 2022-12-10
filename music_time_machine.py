import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_ID = os.environ["SPOTIFY_ID"]
SPOTIFY_SECRET = os.environ["SPOTIFY_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]

# Ask user for date
date = input("What date would you like to travel to?  Please format YYYY-MM-DD\n")

# Get website content
response = requests.get(url=f"{URL}/{date}").text

# Input content and specify parser
soup = BeautifulSoup(response, "html.parser")

# Get song titles
titles = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
# Make new list of song title text, stripping \n & \t chars
title_names = [title.getText().strip("\n\t") for title in titles]

# Connect to Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Get URIs of songs in title_names
song_uris = []

year = date.split("-")[0]

for title in title_names:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist on Spotify.")

# Create playlist
playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100", public=False, description="Music Time Machine")

# Add songs to playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
