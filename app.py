import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')

    download_dir = "/storage/emulated/0/tubemateapp"
    os.makedirs(download_dir, exist_ok=True)  # 👈 create folder if not exists

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{download_dir}/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return jsonify({'status': 'Downloaded to myapptube'})
