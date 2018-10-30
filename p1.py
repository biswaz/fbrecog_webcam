import numpy as np
import cv2
from fbrecog import FBRecog
from config import *

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    path = 'frame.jpg'

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if (k==1048603):    # Esc key to stop
        break
    elif (k==-1):  # normally -1 returned,so don't print it
        continue
    elif (k==1048691): # S key to save
        cv2.imwrite(path, frame)
    else:
        print(k) # else print its value
    # Instantiate the recog class
    recog = FBRecog(access_token, cookie, fb_dtsg)
    # Recog class can be used multiple times with different paths
    print(recog.recognize(path))


# When everything done, release the capture
cap.release()
# Destroy All windows
cv2.destroyAllWindows()
