import subprocess

queries = [
    "Kobe Bryant 710 ESPN LA Mason and Ireland full interview",
    "Kobe Bryant Jim Rome Show full interview uncut",
    "Kobe Bryant Nike launch event press conference uncut",
    "Kobe Bryant All-Star media day uncut interview 2011",
    "Kobe Bryant All-Star media day uncut interview 2016",
    "Kobe Bryant Mamba Sports Academy speech uncut",
    "Kobe Bryant post game press conference USA Spain 2008 uncut",
]

for q in queries:
    cmd = ['yt-dlp', f'ytsearch3:{q}', '--print', '%(id)s | %(title)s | %(duration)s', '--no-playlist']
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(f"\n=== Query: {q} ===")
    for line in res.stdout.strip().splitlines():
        print(" ", line)
