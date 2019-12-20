#source: https://www.geeksforgeeks.org/extract-images-from-video-in-python/

# Importing all necessary libraries
import cv2
import os
import argparse
import glob

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input video file")
ap.add_argument("-t", "--trial", required=False, help="delineates between different vids")
args = vars(ap.parse_args())

# Read the video from specified path
cam = cv2.VideoCapture(args["input"])

try:
	# creating a folder named data
    if not os.path.exists('rgb'):
        os.makedirs('rgb')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

file = open("rgb.txt","w")
file.write("")
file.close()
oldim = glob.glob("rgb/*.jpg")
for im in oldim:
    os.remove(im)

print("Old Files cleaned...")

# frame
currentframe = 0
fps = 30

while(True):

	# reading from frame
    ret,frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './rgb/frame' + str(currentframe/fps) + '.jpg'
        pair = [str(currentframe/fps),str('rgb/frame' + str(currentframe/fps) + '.jpg')]
		# print ('Creating...' + name)

		# writing the extracted images
        cv2.imwrite(name, frame)
        file = open("rgb.txt","a")
        file.write(pair[0]+'    '+pair[1]+'\n')
        file.close()

		# increasing counter so that it will
		# show how many frames are created
        currentframe += 1
    else:
        break

print("New Images Saved...")
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
