import os
from pytube import YouTube
import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})


class Services:

    def video_download(url):
        with ydl:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            video.download()

    def audio_download(url):

        with ydl:
            yt = YouTube(url)
            audio = yt.streams.filter(only_audio=True).first()

            download_file = audio.download()
            base, ext = os.path.splitext(download_file)

            new_file = base + '.mp3'
            os.rename(download_file, new_file)

            new_file
