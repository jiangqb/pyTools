#-*- coding: utf-8 -*-

import os
import cv2

f=open('C:/Users/oops/Desktop/pyTools/XMLParse.txt','r')
fileName='C:/Users/oops/Desktop/pyTools/pos'
count=615
for line in f.readlines():
    Path=line.strip().split(' ')
    print Path
    imagePath=Path[0]
    name=imagePath[-14:]
    x=Path[2]
    y=Path[3]
    width=Path[4]
    height=Path[5]
    print imagePath,x,y,width,height,name
    image=cv2.imread(imagePath)
    number=str(count)
    cv2.imwrite(fileName+'/pos'+number+'.jpg',image[int(y):int(y)+int(height),int(x):int(x)+int(width)])
    count=count+1

# path=f.readline(63)
# print path
# image=cv2.imread(path,1)
# cv2.imwrite(fileName+'/face.jpg',image[30:30+37,375:375+37])
# cv2.imshow('test',cv2.rectangle(image,(375,30),(375+37,30+37),(0,0,255)))
# cv2.waitKey(0)
