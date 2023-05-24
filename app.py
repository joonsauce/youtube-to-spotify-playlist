from spotify_functions import *

while True:
    yt_playlist = input("Please input a link to a YouTube playlist, or enter Q to quit: ")
    if yt_playlist == "Q":
        break

    playlistID = get_playlist_id(yt_playlist)

    if playlistID == -1:
        print("The playlist link is invalid")
        continue

    items = get_items_from_playlist(playlistID)

    if items == -1:
        print('There was a problem retrieving information from YouTube')
        continue

    song_list = get_videos_from_playlist(items)

    if -1 in song_list:
        print("There's been an error retrieving a video from YouTube")
        continue

    songs = [search_spotify(song) for song in song_list]

    if -1 in songs:
        print("There's been an error finding a song from Spotify")
        question = input("Would you like to abort? (y/n)")
        if question == 'y':
            print("Successfully aborted")
            continue
        else:
            songs = [s for s in songs if s != -1]

    playlist_title = get_title_from_playlist(playlistID)

    if playlist_title == -1:
        print("There's been an error getting information from YouTube")

    spotify_playlist_info = create_spotify_playlist(playlist_title)

    if spotify_playlist_info == -1:
        print("There's been an error creating a playlist on Spotify")
        continue

    final = append_to_spotify_playlist(songs, spotify_playlist_info)

    if final == -1:
        print("There's been an error adding songs to playlists to Spotify")
