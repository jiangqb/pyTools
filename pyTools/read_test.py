# -*- coding: utf-8 -*-

import os,sys
from os.path import isfile,isdir,join

'''f=open('C:/Users/oops/Desktop/result.txt','w')
FindPath='G:/work3/MultiPIE/data/'
FileList=[]
FileName=os.listdir(FindPath)   #FindPath路径下的文件名称
print(FileName)
if(len(FileName)>0):
    for fn in FileName:
        #FindPath=os.path.join(FindPath,fn)
        print(os.path.join(FindPath,fn))
        if(os.path.isdir(FindPath+'/'+fn)):
            FindPath=FindPath+'/'+fn
            FileName=os.listdir(FindPath)
            print(FileName)
        #print(os.path.join(os.path.join(FindPath,fn),fn))
        FileList.append(os.path.join(FindPath,fn))
    print FileList
        #if os.path.isdir(FindPath):
            #dirname=os.listdir(FindPath)
            #print(dirname)
            #FindPath=os.path.join(FindPath,dirname)
            #print(FindPath)
        #FullFileName=os.path.join(FindPath,fn)   #拼接完整文件路径（绝对路径）
        #print(FullFileName)
        #f.write(FullFileName+'\n')   #将FindPath路径下所有文件的完整路径写入result.txt文件中
        #FileList.append(FullFileName)
        #print(FileList[0])
        #f.write(FileList[0]+'\n')   #选择写入第一个文件的完整路径
'''
root='G:/Face Detection Database/FDDB/originalPics'
f=open('C:/Users/oops/Desktop/pyTools/result.txt','w')

for parent,dirNames,fileNames in os.walk(root):
    for fileName in fileNames:
        absFileName = os.path.join(parent +'\\'+ fileName)
        print absFileName
        #print absFileName[-25:-21] ,absFileName[-6:-4]
        #if absFileName[-6:-4]=='01' and int(absFileName[-14:-11])>346:
            #print absFileName[-14:-11]
        f.write(absFileName+'\n')


