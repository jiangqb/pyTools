import cv2
import os
import imghdr
import random
#file_dirs contains all the images
#root_file_dir contains all the file_dirs
root_file_dir="/media/brl/JQB/sequence/biker/biker"
file_dirs=os.listdir(root_file_dir)
storage_path="/home/brl/video"
for one_of_file_dir in file_dirs:
    file_dir=root_file_dir+os.path.sep+one_of_file_dir
    if os.path.isdir(file_dir):
        allImage=os.listdir(file_dir)
        allImage.sort()
        randId=random.randint(0,len(allImage)-1)
        # to obtain the w,h of the iamges
        # to check whether the file can be imread()
        while os.path.isdir(file_dir+os.path.sep+allImage[randId]) \
        or imghdr.what(file_dir+os.path.sep+allImage[randId])==None:
            randId = random.randint(0, len(allImage)-1)
        img_file=cv2.imread(file_dir+os.path.sep+allImage[1])
        myVideo=cv2.VideoWriter(storage_path+os.path.sep+file_dir.split(os.path.sep)[-1]+".avi",cv2.cv.CV_FOURCC('M','J','P','G'),30,(img_file.shape[1],img_file.shape[0]),True)
        for image in allImage:
            if os.path.isdir(file_dir+os.path.sep+image)==False \
            and imghdr.what(file_dir+os.path.sep+image)!=None:
              myVideo.write(cv2.imread(file_dir+os.path.sep+image))
