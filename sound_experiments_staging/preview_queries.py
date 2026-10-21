import subprocess

queries = [
    "Kobe Bryant Jimmy Fallon full interview",
    "Kobe Bryant Conan OBrien full interview",
    "Kobe Bryant Jay Leno full interview",
    "Kobe Bryant press conference uncut 2010 finals Game 7",
    "Kobe Bryant post game press conference 2000 finals",
]

for q in queries:
    cmd = ['yt-dlp', f'ytsearch3:{q}', '--print', '%(id)s | %(title)s | %(duration)s', '--no-playlist']
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(f"\n=== Query: {q} ===")
    for line in res.stdout.strip().splitlines():
        print(" ", line)
