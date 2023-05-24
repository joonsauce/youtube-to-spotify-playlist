from settings import *


def get_playlist_id(url: str):
    sp = url.split('?')
    if 'https://music.youtube.com/playlist' not in sp or 'https://youtube.com/playlist' not in sp and len(sp) == 1:
        return -1
    query = sp[1]
    queries = query.split('&')
    l_id = queries[0]
    sp2 = l_id.split('list=')
    return sp2[1]


def get_title_from_playlist(playlistID):
    playlist_url = 'https://www.googleapis.com/youtube/v3/playlists'
    link = playlist_url +'?part=snippet&id={0}&maxResults=50&key={1}'.format(playlistID, youtube_key)
    response = requests.get(link)
    if response.status_code != 200:
        return -1
    return response.json()['items'][0]['snippet']['title']


def get_items_from_playlist(playlistID):
    playlist_item_url = 'https://www.googleapis.com/youtube/v3/playlistItems'
    link = playlist_item_url + '?part=contentDetails&playlistId={0}&maxResults=50&key={1}'.format(playlistID, youtube_key)
    response = requests.get(link)
    if response.status_code != 200:
        return -1
    value = response.json()
    items = response.json()['items']

    if 'nextPageToken' in list(value.keys()):
        return items + multipage(playlistID, value['nextPageToken'])

    return items


def get_videos_from_playlist(items):
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    song_list = list()

    for item in items:
        video = item['contentDetails']['videoId']
        new_link = video_url + '?part=snippet&id={0}&key={1}'.format(video, youtube_key)
        new_response = requests.get(new_link)
        if new_response.status_code != 200:
            song_list.append(-1)
        else:
            new_vals = new_response.json()
            title = new_vals['items'][0]['snippet']['title']
            channel = new_vals['items'][0]['snippet']['channelTitle']
            new = channel.split(' - ')[0] + ' - ' + title
            song_list.append(new)

    return song_list


def multipage(playlistID, token):
    playlist_item_url = 'https://www.googleapis.com/youtube/v3/playlistItems'
    link = playlist_item_url + '?part=contentDetails&playlistId={0}&pageToken={1}&maxResults=50&key={2}'.format(
        playlistID, token, youtube_key)
    response = requests.get(link)
    value = response.json()
    items = response.json()['items']

    if 'nextPageToken' in list(value.keys()):
        return items + multipage(playlistID, value['nextPageToken'])

    return items
