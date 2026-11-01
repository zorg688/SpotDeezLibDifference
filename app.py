from src.spotify import spotify_auth, spotify_client
from src.deezer import deezer_client


sp = spotify_auth.authenticate_spotify()

shows, artists_with_albums, unsaved_artists_with_albums = spotify_client.collect_artists_shows_and_albums(sp=sp)

print("Collected authenticated user's artists, albums and podcasts!\n\nNow comparing the artists list to Deezer...")


only_artists = list(artists_with_albums.keys())

validated_artists = deezer_client.deezer_artists(only_artists)

for artist, validated in zip(only_artists, validated_artists):
    print(f'{artist}: {validated}')
