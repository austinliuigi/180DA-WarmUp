# Sources: https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Get user input for portion of image
prompt = "Enter size of rect: "
rect_size = list(map(int, input(prompt).split()))

capture = cv2.VideoCapture(0)
_, frame = capture.read()

width = frame.shape[1]
height = frame.shape[0]
center = (width/2, height/2)

tl = (int(center[0]-rect_size[0]/2), int(center[1]-rect_size[1]/2))
br = (int(center[0]+rect_size[0]/2), int(center[1]+rect_size[1]/2))


blank = np.zeros((rect_size[1], rect_size[0], 3), dtype='uint8')

while True:
    _, frame = capture.read()

    # Extract region of interest
    frame_selection = frame[tl[1]:br[1], tl[0]:br[0]]
    frame_selection = cv2.cvtColor(frame_selection, cv2.COLOR_BGR2RGB)
    # cv2.imshow("frame_selection", frame_selection)

    # Draw rect on frame
    cv2.rectangle(frame, (tl[0], tl[1]), (br[0], br[1]), (0, 0, 255))
    cv2.imshow("frame", frame)

    # Press 'u' to update dominant color window
    if cv2.waitKey(1) == ord("u"):
        # Convert from 2D matrix of 3-elem list to array of 3-elem list
        frame_selection = frame_selection.reshape((frame_selection.shape[0] * frame_selection.shape[1], 3))
        kmeans = KMeans(n_clusters=2) #cluster number
        kmeans.fit(frame_selection)

        blank[0:rect_size[1]//2] = kmeans.cluster_centers_[0]
        blank[rect_size[1]//2:rect_size[1]] = kmeans.cluster_centers_[1]
        blank = cv2.cvtColor(blank, cv2.COLOR_BGR2RGB)
        cv2.imshow("blank", blank)

    if cv2.waitKey(1) == ord("q"):
        break
