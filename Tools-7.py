import youtube_dl

import youtube_dl

options = {
    'format': 'bestaudio/best',  # choice of quality
    'extractaudio': True,        # only keep the audio
    'audioformat': "mp3",        # convert to mp3
    'outtmpl': '%(id)s',         # name the file the ID of the video
    'noplaylist': True,          # only download single song, not playlist
    'listformats': True,         # print a list of the formats to stdout and exit
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])