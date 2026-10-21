import sqlite3
import os

db_path = r'E:\Sound Experiments\Kobe bryant Database raw\_catalog\catalog.sqlite'
conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute('''
    SELECT s.id, s.title, s.platform_id, r.file_path 
    FROM sources s 
    JOIN raw_files r ON r.source_id = s.id 
    WHERE s.title LIKE '%Dear Basketball%' 
       OR s.title LIKE '%retirement%' 
       OR s.title LIKE '%Oscar%'
       OR s.title LIKE '%speech%'
       OR s.title LIKE '%Mamba Out%'
    LIMIT 30
''')

for row in c.fetchall():
    print(f"ID: {row[0]} | Title: {row[1]}")
    print(f"   PlatformID: {row[2]}")
    print(f"   Path: {row[3]}")
    print("-" * 50)
