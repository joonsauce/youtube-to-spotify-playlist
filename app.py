from functions import *

while True:
    yt_playlist = input("Please input a link to a YouTube playlist, or enter Q to quit: ")
    if yt_playlist == "Q":
        break
    info = get_info(yt_playlist)
    if info == -1:
        print("The playlist link is invalid or cannot be reached at the moment")
        continue
    elif info == -2:
        print("There was an error retrieving information from the playlist")
        continue
    elif info == -3:
        print("The YouTube link is not a link to a playlist")
        continue

    song_info = get_info_from_yt(info)

    songs = [search_spotify(song) for song in song_info]

    spotify_playlist_info = create_spotify_playlist(info['title'])

    append_to_spotify_playlist(songs, spotify_playlist_info)

