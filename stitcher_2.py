from imutils import paths
import imutils
import cv2
import sys
import numpy as np
import os

positions = []
for arg in sys.argv[1:]:
    positions.append(arg)

all_frames = []

# EXTRACT
for position in positions:
    print('Extracting frames from: ' + position)
    #read the video
    vid = cv2.VideoCapture(position)
    #frame counter
    frame_index = 0
    frames = []

    while(True):
        success, frame = vid.read()
        #condition for end of video
        if not success: 
            break

        #append each frame in the instance of the frames list
        frames.append(frame)

        # next frame
        #or we can skip n frames by doing + n
        frame_index += 1
    #append the entire list to the list of aggregates
    all_frames.append(frames)

print('Attempting to stitch frames')
# STITCH
zippy = list(zip(*all_frames))
# initialize OpenCV's image stitcher object and then process the image
stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()

#make stitched frame directory
path = 'stitched_frames/'
if not os.path.exists(path):
    os.makedirs(path)

counter = 0
stitched_frames = []
for frame_set in zippy:
    (status, stitched) = stitcher.stitch(list(frame_set))
    # if the status is '0', then OpenCV successfully performed image
    # stitching
    if status == 0:
        # write the output stitched image to disk
        name = path + 'frame_' + str(counter) + '.jpg'
        print ('Creating... frame ' + str(counter))
        cv2.imwrite(name, stitched)
        # stitched_frames.append(stitched)
        if(counter == 0):
            stitched_frames.append(stitched)

    # otherwise the stitching failed, likely due to not enough keypoints)
    # being detected
    else:
        print('[INFO] frame ' + str(counter) +  " stitching failed ({})".format(status))
    counter+=1

#CONSTRUCT VIDEO

print('DONE')