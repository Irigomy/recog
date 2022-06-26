import cv2
import face_recognition as fc
import pickle
from imutils import paths
import os

model_path = list(paths.list_images("media/models"))
print(model_path)
KnownEncoding = []
names = []
for(i, model_path) in enumerate(model_path):
	print("looping")
	name = model_path.split(os.path.sep) [-2]
	print("split")
	image = cv2.imread(model_path)
	print("cv read")
	convert_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	print("convert rgb")
	boxes = fc.face_locations(convert_rgb, model="cnn")
	print("boxes cnn")
	encodings = fc.face_encodings(convert_rgb, boxes) 
	print("encoding")
	for encoding in encodings:
			print("looping encoding")
			KnownEncoding.append(encoding)
			names.append(name)
			data = {"encodings": KnownEncoding, "names": names}
			f = open("encoding.pickle", "wb")
			f.write(pickle.dumps(data))
			f.close()
			print("succes")