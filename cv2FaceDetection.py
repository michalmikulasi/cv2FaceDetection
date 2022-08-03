#importing libraries
import os
import pydoc
from tkinter.tix import INTEGER
import cv2

#importing the haar cascade face detector
haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


#capturing the video from the webcam
def funkcia(grey, frame):
    faces = haar_face_cascade.detectMultiScale(grey, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_grey = grey[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_grey, 1.1, 3)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
    return frame

#capturing the video from the webcam and displaying it
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = funkcia(grey, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

#generating documentation for the function
def get_pydoc_text(module):
    "Returns pydoc generated output as text"
    doc = pydoc.TextDoc()
    loc = doc.getdocloc(pydoc_mod) or ""
    if loc:
        loc = "\nMODULE DOCS\n    " + loc + "\n"

    output = doc.docmodule(module)

    # cleanup the extra text formatting that pydoc preforms
    patt = re.compile('\b.')
    output = patt.sub('', output)
    return output.strip(), loc


range.__doc__
range(stop) 
range(start, stop, [step])
