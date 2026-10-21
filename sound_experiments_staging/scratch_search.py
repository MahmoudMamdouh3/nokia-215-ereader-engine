import subprocess

cmd = ['yt-dlp', 'ytsearch10:KB24KZ Kobe Doin Work', '--print', '%(id)s | %(title)s | %(uploader)s', '--no-playlist']
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)
