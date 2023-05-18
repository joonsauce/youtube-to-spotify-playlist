from spotify_auth import *

def get_info_from_yt(info):
    song_information = []
    for i in info['entries']:
        song_information.append(i['artist']+' - '+i['title'])
    return song_information

def get_info(msg):
    try:
        requests.get(msg)
    except:
        return -1
    else:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(msg, download=False)
        except:
            return -2
        else:
            return check_playlist(info)

# this is mostly just a test function
def get_user_id():
    scope = 'user-read-private user-read-email'

    print("Please authenticate use using this link: {}".format(generate_auth_link(scope)))

    new_link = input("Please input the callback url here: ")

    spotify_code = new_link.split('?code=')[1]

    headers = {
        'Authorization': 'Bearer {}'.format(get_authorized_spotify_token(spotify_code)),
    }

    response = requests.get('https://api.spotify.com/v1/me', headers=headers)

    if response.status_code != 200:
        return -1
    return response.json()

def check_playlist(info):
    keys = list(info.keys())
    if 'entries' not in keys:
        return -3
    return info

def create_spotify_playlist(title):
    scope = 'playlist-modify-public playlist-modify-private'

    print("Please authenticate use using this link: {}".format(generate_auth_link(scope)))

    new_link = input("Please input the callback url here: ")

    spotify_code = new_link.split('?code=')[1]

    token = get_authorized_spotify_token(spotify_code)

    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Content-Type': 'application/json'
    }

    data = {
        'name': title,
        'description': 'converted playlist',
        'public': False
    }

    response = requests.post('https://api.spotify.com/v1/users/{}/playlists'.format(spotify_user_id), headers=headers,
                             json=data)

    if response.status_code != 201:
        return -1

    return [response.json(), token]

def search_spotify(song):
    headers = {
        'Authorization': 'Bearer {}'.format(get_basic_spotify_token())
    }
    query = parse.urlencode({'q': song})

    response = requests.get('https://api.spotify.com/v1/search?'+query+'&type=track', headers=headers)

    if response.status_code != 200:
        return -1

    return response.json()['tracks']['items'][0]['id']

def append_to_spotify_playlist(songs, info):
    playlist_id = info[0]['id']
    token = info[1]

    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Content-Type': 'application/json'
    }

    data = {
        'uris': ['spotify:track:{}'.format(i) for i in songs],
        'position': 0
    }

    response = requests.post('https://api.spotify.com/v1/playlists/{}/tracks'.format(playlist_id), headers=headers,
                             json=data)

    if response.status_code != 201:
        return -1

    return response.json()