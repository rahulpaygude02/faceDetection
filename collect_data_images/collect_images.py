#from mtcnn.mtcnn import MTCNN

import numpy as np
import cv2
import os
from datetime import datetime

class Datacollector:

    def __init__(self, args):
        self.args = args
        # Detector = mtcnn_detector
        #self.detector = MTCNN()

    def collectImagesFromCamera(self):
        # initialize video stream
        cap = cv2.VideoCapture(0)

        # Setup some useful var
        faces = 0
        frames = 0
        max_faces = int(self.args["faces"])
        #max_bbox = np.zeros(4)
        
        if not (os.path.exists(self.args["output"])):
            os.makedirs(self.args["output"])

        while faces < max_faces:
            ret, frame = cap.read()
            frames += 1
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            dtString = str(datetime.now().microsecond)

            
            # Get all faces on current frame
            #bboxes = self.detector.detect_faces(frame)
            cv2.imwrite(os.path.join(self.args["output"], "img.jpg"),frame)

            print("[INFO] {} Image Captured".format(faces + 1))
            faces += 1

            cv2.imshow("Face detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

