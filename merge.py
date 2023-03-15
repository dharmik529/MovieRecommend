import csv
import sqlite3
import json

conn = sqlite3.connect('data/data.db')
cur = conn.cursor()

cur.execute("SELECT original_title, genres, keywords, overview FROM movies;")
output = cur.fetchall()

tags = []

for out in output:
    genres = []
    keywords = []

    genre_json = json.loads(out[1])
    keywords_json = json.loads(out[2])
    overview = out[3]
    for i in genre_json:
        genres.append(i['name'])
    for i in keywords_json:
        keywords.append(i['name'])

    cur.execute(f'SELECT * FROM credits WHERE title = "{out[0]}";')
    movoutput = cur.fetchall()
    cast = []
    crew = []
    if movoutput:
        id = movoutput[0][0]
        title = movoutput[0][1]
        cast_json = json.loads(movoutput[0][2])
        crew_json = json.loads(movoutput[0][3])

        for p in cast_json:
            cast.append(p['name'])

        for i in crew_json:
            if i['job'] == 'Director':
                crew.append(i['name'])
        tag = title + ' ' + overview + ' ' + ' '.join(str(e) for e in cast) + ' ' + ' '.join(str(r) for r in crew)
        tags.append([id, title, tag])
    else:
        continue
    
with open("data/tags.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(tags)
