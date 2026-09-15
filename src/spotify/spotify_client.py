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


prev_last_artist = None
current_last_artist = None

while current_last_artist is None or current_last_artist != prev_last_artist:

    prev_last_artist = current_last_artist

    results = sp.current_user_followed_artists(limit =50, after=prev_last_artist)

    if len(results['artists']['items']) <1:
        print('---------------------------------')
        print("That's it!")
        break

    current_last_artist = results['artists']['items'][-1]['id']

    

    for item in results['artists']['items']:
        print(item['name'])
    

results = sp.current_user_saved_shows(limit=50)

for element in results['items']:
    print(element['show']['name'])


print("------------------That's it!-----------------")