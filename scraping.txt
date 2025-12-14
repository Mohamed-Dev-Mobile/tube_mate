
import yt_dlp

url = "https://www.youtube.com/live/ZVf9yWOnAic?si=SwnX7dNP5fOLQNBI"

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': r'E:\Downloads\%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])