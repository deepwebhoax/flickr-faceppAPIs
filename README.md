<h1>DATABASE</h1>
<p>We were using sqlite3 database. It contains two tables: faces, photos. </p>

<p>Also there are three Python scripts:
 <p>1. album_download.py
    Contains function which provides availability of certain photos from flickr.com to other scripts by storing there urls in a database. </p>
<p> 2. face_nice.py
    Contains function which fills the database with photo-analysis results provided by facial recognition service Detect API by faceplusplus.com.</p>
<p> 3. twelve_threads.py
    Calls the above functions. Utilizes multithreading.</p>
 </p>

<p>For more detailed desciption view comments in there code.</p>
