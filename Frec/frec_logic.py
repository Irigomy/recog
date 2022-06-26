import face_recognition as fc
import pickle
import os
from django.conf import settings

	

class Facerec(object):
    def __init__(self):
        self.encoding = pickle.loads(
            open(os.path.sep.join([settings.BASE_DIR, "encoding.pickle"]), "rb").read()
        )
    def face_recognition(self, frame):
        locations = fc.face_locations(frame, model="cnn")
        encodings = fc.face_encodings(frame, locations)
        for face_encoding in encodings:
            matches = fc.compare_faces(self.encoding["encodings"], face_encoding, 0.6)
            names = "Anjeng"
            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                for i in matchedIdxs:
                    names = self.encoding["names"][i]
            return names

    def get_frame(self, frame):
        preds = self.face_recognition(frame=frame)
        return preds

		




