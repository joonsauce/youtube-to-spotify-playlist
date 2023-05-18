from base64_convert import *
from settings import *

def generate_auth_link(scope):
    information = {'response_type': 'code', "client_id": spotify_id, "scope": scope, "redirect_uri": "http://127.0.0.1:5000/callback"}
    query = parse.urlencode(information)
    return "https://accounts.spotify.com/authorize?"+query

def get_authorized_spotify_token(spotify_code):
    spotify_data = {
        'grant_type': 'authorization_code',
        'code': spotify_code,
        'redirect_uri': "http://127.0.0.1:5000/callback"
    }

    headers = {
        'Authorization': 'Basic {}'.format(convert(spotify_id+":"+spotify_token)),
    }

    response = requests.post('https://accounts.spotify.com/api/token', data=spotify_data, headers=headers)

    if response.status_code != 200:
        return -1

    return response.json()['access_token']

def get_basic_spotify_token():
    spotify_data = {
        'grant_type': 'client_credentials',
        'client_id': spotify_id,
        'client_secret': spotify_token
    }

    response = requests.post('https://accounts.spotify.com/api/token', data=spotify_data)

    if response.status_code != 200:
        return -1
    return response.json()['access_token']