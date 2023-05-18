# youtube-to-spotify-playlist
Convert YouTube Music playlists into Spotify playlists

## Requirements
- A Spotify developer account with an application setup
  - You will need the Client ID and Client Secret from the settings menu of the application
  - You need to place these under spotify_id and spotify_token in `secret.py`
- A Spotify user account
  - You will need to place the user id into spotify_user_id in `secret.py`
- The libraries as outlined in `requirements.txt`
## Future Plans
- Use the YouTube API instead of yt_dlp -> yt_dlp unnecessarily slows down the processing speed
- Put this into a website -> a much nicer UI to work with
