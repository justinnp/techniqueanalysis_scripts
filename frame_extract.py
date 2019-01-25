import cv2
import sys
import numpy as np
import os

positions = []
for arg in sys.argv[1:]:
    positions.append(arg)

for position in positions :

    #remove extension from video to save as file name
    video_name = position
    no_period = video_name.index('.')
    video_name_wo_ext = video_name[:no_period]

    #read the video
    vid = cv2.VideoCapture(position)

    #create the path name where the frames will be stored
    path = video_name_wo_ext + '_' + 'frames'

    #if the path name doesn't exist make it
    if not os.path.exists(path):
        os.makedirs(path)

    #frame counter
    frame_index = 0

    while(True):
        success, frame = vid.read()
        #condition for end of video
        if not success: 
            break

        #add the frame to the path
        name = './' + path + '/frame' + str(frame_index) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

        # next frame
        #or we can skip n frames by doing + n
        frame_index += 1