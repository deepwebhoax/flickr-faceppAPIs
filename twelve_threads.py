import face_nice as face
import album_download as ad
import _thread
import time

_thread.start_new_thread(ad.album_url, (ad.set_id,))

time.sleep(2)
_thread.start_new_thread(face.evaluate_emotions, (face.our_db, 1, 11))
_thread.start_new_thread(face.evaluate_emotions, (face.our_db, 2, 11))
_thread.start_new_thread(face.evaluate_emotions, (face.our_db, 3, 11))
_thread.start_new_thread(face.evaluate_emotions, (face.our_db, 4, 11))
_thread.start_new_thread(face.evaluate_emotions, (face.our_db, 5, 11))
_thread.start_new_thread(face.evaluate_emotions, (face.our_db, 6, 11))
_thread.start_new_thread(face.evaluate_emotions, (face.our_db, 7, 11))
_thread.start_new_thread(face.evaluate_emotions, (face.our_db, 8, 11))
_thread.start_new_thread(face.evaluate_emotions, (face.our_db, 9, 11))
_thread.start_new_thread(face.evaluate_emotions, (face.our_db, 10, 11))

face.evaluate_emotions(face.our_db, 11, 11)
