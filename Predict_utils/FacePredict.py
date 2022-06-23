from deepface import DeepFace
import cv2
import os
#from datetime import datetime
import time
import shutil

class FacePredict:
    def __init__(self,args):
        self.args = args
        self.model_name = 'VGG-Face'
        

    def detectFace(self):
        if os.path.isdir(self.args["temp"]):
            shutil.rmtree(self.args["temp"])

        cap = cv2.VideoCapture(0)

        # Setup some useful var
        faces = 0
        frames = 0
        max_faces = 2
        

        if not (os.path.exists(self.args["temp"])):
            os.makedirs(self.args["temp"])

        while faces < max_faces:
            ret, frame = cap.read()
            frames += 1
                       
            time.sleep(1)
            # Get all faces on current frame
            #bboxes = self.detector.detect_faces(frame)
            cv2.imwrite(os.path.join(self.args["temp"], "image.jpg"),frame)

            faces += 1

            cv2.imshow("Face detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        img1_path = "F:/faceDetection/datasets/temp/image.jpg"
        img2_path = os.path.join(self.args["output"],"img.jpg")

        resp = DeepFace.verify(img1_path = img1_path, img2_path = img2_path ,model_name = self.model_name,enforce_detection=False)
        print(resp)
        
        varify = resp["verified"]
        return varify

    




        




