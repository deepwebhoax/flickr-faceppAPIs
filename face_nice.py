from os import listdir
import json
import requests
from requests_toolbelt import MultipartEncoder
import sqlite3
import time

# Request target url.
facepp_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'

# My personal face++ user keys.
key = "xSEonOy5LV3UxX8TCjxA4cuB-2rDfWxk"
secret = "klLItU8XQ32F0u-mh8Wvf5o5PDRI4zss"

photos_count = 289
# Free version limits.
max_faces = 5

# Target database.
our_db = 'photos.db'

# start - start index (for multithreading)
def evaluate_emotions(db_name, start, thread_count):
    """
    Given the database db_name having photos_count "photos" table with photo_id, photo_url
    and faces table with anger, disgust, fear, happiness, neutral, sadness,
    surprise, width, top, left, height columns
    creates records in faces using Detect API by Face++.

    An emotion value of a photo is the mean of this emotion's values of all faces.
    """
    # Connecting to database
    con = sqlite3.connect(db_name)
    ri = start
    while ri<photos_count:
        print(ri, start)
        # Getting photo id and url
        cur = con.cursor()
        id_url = cur.execute("SELECT photo_id, photo_url FROM photos WHERE rowid=?", (ri,)).fetchone()
        check = cur.execute("SELECT sadness FROM faces WHERE photo_id=?", (id_url[0],)).fetchone()
        cur.close()
        ri+= thread_count
        if check:
            continue

        # Making a POST request. r contains the response
        d = {'api_key': key, 'api_secret': secret, 'image_url': id_url[1], 'return_attributes':'emotion'}
        r = requests.post(facepp_url, data=d)
        while r.status_code!=200:
            r = requests.post(facepp_url, data=d)

        # Extracting faces' emotions values from response json.
        faces_count = len(r.json()['faces'])
        if faces_count==0:
            continue
        emotions = [face["attributes"]["emotion"] for face in r.json()['faces'][:max_faces]]
        rectangles = [face["face_rectangle"] for face in r.json()['faces'][:max_faces]]

        # Filling recognized faces' emotions and coordinates into faces table
        cur = con.cursor()
        for i in range(len(emotions)):
            cur.execute("""INSERT INTO faces
                         VALUES  (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (id_url[0], emotions[i]['sadness'], emotions[i]['neutral'], emotions[i]['disgust'],
                         emotions[i]['anger'], emotions[i]['surprise'], emotions[i]['fear'], emotions[i]['happiness'],
                         rectangles[i]['width'], rectangles[i]['top'],rectangles[i]['left'], rectangles[i]['height']))
        con.commit()
        cur.close()
