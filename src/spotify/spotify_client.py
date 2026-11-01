import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

REDIRECT_URI = os.getenv('REDIRECT_URL')
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SCOPE = os.getenv('SCOPE')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))


print('-----------Artists-------------')

prev_last_artist = None
current_last_artist = None


while current_last_artist is None or current_last_artist != prev_last_artist:

    prev_last_artist = current_last_artist

    results = sp.current_user_followed_artists(limit =50, after=prev_last_artist)

    if len(results['artists']['items']) <1:
        break

    current_last_artist = results['artists']['items'][-1]['id']

    

    for item in results['artists']['items']:
        print(item['name'])

print('---------------------------------')
print("That's all artists!\n")
    

print('-----------Podcasts/Shows-------------')

prev_last_show_index = 0
current_last_show_index = 0

while current_last_show_index == 0 or current_last_show_index != prev_last_show_index:

    prev_last_show_index = current_last_show_index

    results = sp.current_user_saved_shows(limit=50, offset=prev_last_show_index)

    if len(results['items']) <1:
        break

    current_last_show_index = prev_last_show_index + len(results['items'])


    for element in results['items']:

        print(element['show']['name'])
    

print("------------------That's all Podacsts/Shows!-----------------")