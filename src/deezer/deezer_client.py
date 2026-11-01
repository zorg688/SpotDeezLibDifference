import requests

def deezer_artists(artists) -> list:

    #artists = ['Amon Amarth', 'Ice Nine Kills', 'Daniel Pietschke the 18th']

    valid_artists = [False]*len(artists)

    all_artists = len(artists)

    for artist_index, artist in enumerate(artists):

        print(f'Working on artist {artist_index+1}/{all_artists}', end = '\r')

        short_artist = ''.join(artist.split(" ")).lower()
        
        r= requests.get(f'https://api.deezer.com/search/artist?q={short_artist}')

        artists_search = []

        while True:
            
            for index in range(len(r.json()['data'])):
                
                artists_search.append(r.json()['data'][index]['name'])
                '''
                for element in album:
                    if element == 'artist':
                        print(element, r.json()['data'][index][element]['name'])
                    else:
                        print(element, r.json()['data'][index][element])
                '''
                
            try:
                r = requests.get(r.json()['next'])
            except:
                break
        
        if artist in artists_search:
            valid_artists[artist_index] = True

    print()
    return valid_artists




if __name__ == "__main__":
    deezer_artists([])