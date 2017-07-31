# -*- coding:utf-8 -*-

import os,sys,cv2
from os.path import isfile,isdir,join

root='H:\Multi-Pie\data\session02\multiview'
savePath='H:/result/session02/'

i=1
while i<=250:
    if i<10:
        path=(savePath+'00'+str(i))
    elif i<100:
        path=(savePath+'0'+str(i))
    else:
        path=(savePath+str(i))
    os.mkdir(path)
    i=i+1

for parent,dirNames,fileNames in os.walk(root):
    for fileName in fileNames:
        absFileName=os.path.join(parent+'\\'+fileName)
        if absFileName[-13:-11]=='01' and absFileName[-10:-7]=='051':
            imagePath=absFileName
            print imagePath
            image = cv2.imread(imagePath, 1)
            number=imagePath[-20:-17]
            print number,type(number),path
            j=1
            while j<=250:
                if j<10:
                    fn=savePath+'00'+str(j)
                elif j<100:
                    fn=savePath+'0'+str(j)
                else:
                    fn=savePath+str(j)
                j=j+1
                if number==fn[-3:]:
                    cv2.imwrite(fn + '/' + imagePath[-20:], image)
            # if number==path[-3:]:
            #     cv2.imwrite(path+'/'+imagePath[-20:],image)
            # image=cv2.imread(imagePath,1)
            # cv2.imwrite()
