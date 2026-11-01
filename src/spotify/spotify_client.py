

def spotify_bands(sp) -> list:
    print('-----------Artists-------------')

    prev_last_artist = None
    current_last_artist = None
    artists = []


    while current_last_artist is None or current_last_artist != prev_last_artist:

        prev_last_artist = current_last_artist

        results = sp.current_user_followed_artists(limit =50, after=prev_last_artist)

        if len(results['artists']['items']) <1:
            break

        current_last_artist = results['artists']['items'][-1]['id']

        

        for item in results['artists']['items']:
            artists.append(item['name'])

    print('---------------All artists appended------------------')

    return artists
    

def spotify_shows(sp) -> list:
    print('-----------Podcasts/Shows-------------')

    prev_last_show_index = 0
    current_last_show_index = 0
    shows = []

    while current_last_show_index == 0 or current_last_show_index != prev_last_show_index:

        prev_last_show_index = current_last_show_index


        results = sp.current_user_saved_shows(limit=3, offset=prev_last_show_index)
        
        if len(results['items']) <1:
            break

        current_last_show_index = prev_last_show_index + len(results['items'])


        for element in results['items']:

            shows.append(element['show']['name'])
            
        

    print("------------------That's all Podacsts/Shows!-----------------")

    return shows

#return dictionary with album names as keys and lists of artists as values
def spotify_albums(sp) -> dict:
    print('-----------Albums-------------')

    prev_last_album_index = 0
    current_last_album_index = 0
    albums = {}

    while current_last_album_index == 0 or current_last_album_index != prev_last_album_index:

        prev_last_album_index = current_last_album_index

        results = sp.current_user_saved_albums(limit=50, offset=prev_last_album_index)

        if len(results['items']) <1:
            break

        current_last_album_index = prev_last_album_index + len(results['items'])


        for element in results['items']:

            album_artists = []

            for artists in element['album']['artists']:
                album_artists.append(artists['name'])
            albums[element['album']['name']] = album_artists
        
    print("------------------That's all Albums!-----------------")

    return albums

#returns a dictonary with artists as keys and albums as values
def assign_artists_to_albums(artists, albums_with_artists) -> tuple[dict, dict]:

    artists_with_albums = {element: [] for element in artists}
    unsaved_artists_with_albums = {'Unknown':[]}

    for album in albums_with_artists:
        for artist in albums_with_artists[album]:
            if artist in artists_with_albums.keys():
                artists_with_albums[artist].append(album)
            elif artist in unsaved_artists_with_albums.keys():
                unsaved_artists_with_albums[artist].append(album)
            else:
                unsaved_artists_with_albums.update({artist:[album]})
    
    return artists_with_albums, unsaved_artists_with_albums
                

def collect_artists_shows_and_albums(sp) -> tuple[list, dict, dict]:
    artists = spotify_bands(sp=sp)
    shows = spotify_shows(sp=sp)
    albums_with_artists = spotify_albums(sp=sp)

    artists_with_albums, unsaved_artists_with_albums = assign_artists_to_albums(artists=artists, albums_with_artists=albums_with_artists)

    return shows, artists_with_albums, unsaved_artists_with_albums

if __name__ == "__main__":

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

    artists = spotify_bands(sp=sp)
    shows = spotify_shows(sp=sp)
    albums_with_artists = spotify_albums(sp=sp)

    artists_with_albums, unsaved_artists_with_albums = assign_artists_to_albums(artists=artists, albums_with_artists=albums_with_artists)

    print(artists_with_albums)