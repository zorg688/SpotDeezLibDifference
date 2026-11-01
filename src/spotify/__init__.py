import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import spotify_client

load_dotenv()



REDIRECT_URI = os.getenv('REDIRECT_URL')
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SCOPE = os.getenv('SCOPE')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))


def collect_artists_shows_and_albums():
    artists = spotify_client.spotify_bands(sp=sp)
    shows = spotify_client.spotify_shows(sp=sp)
    albums_with_artists = spotify_client.spotify_albums(sp=sp)

    artists_with_albums, unsaved_artists_with_albums = spotify_client.assign_arists_to_albums(artists=artists, albums_with_artists=albums_with_artists)

    return shows, artists_with_albums, unsaved_artists_with_albums