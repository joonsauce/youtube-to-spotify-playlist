import base64
import requests
from urllib import parse
import yt_dlp
from secret import *

ydl_opts = {
    'skip_download': 'True',
}
