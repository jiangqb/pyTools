# -*- coding: utf-8 -*-

import os,sys
from os.path import isfile,isdir,join
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

root='C:/Users/oops/Desktop/new_labels'
f=open('C:/Users/oops/Desktop/XMLParse.txt','w')

for parent,dirNames,fileNames in os.walk(root):
    for fileName in fileNames:
        absFileName=os.path.join(parent+'/'+fileName)
        #print absFileName
        tree=ET.ElementTree(file=absFileName)
        treeRoot=tree.getroot()
        #print treeRoot.tag,treeRoot.attrib
        for rootChild in treeRoot:
            # print rootChild.tag,rootChild.attrib
            if rootChild.tag=='path':
                PicPath=rootChild.text
            # elif rootChild.tag == 'filename':
            #     FileName = rootChild.text
            #     f = open('C:/Users/oops/Desktop/new_file/' + FileName + '.txt', 'w')
            elif rootChild.tag=='object':
                for child in rootChild:
                    if child.tag=='pose':
                        facePose=child.text.split(' ')
                        print facePose,PicPath
                    if child.tag=='bndbox':
                        '''if facePose[0] == '0' and facePose[2] == '0' and int(facePose[1]) >= -30 and int(
                                facePose[1]) <= 30:'''
                        f.write(PicPath+' 1 ')
                        for kids in child:
                            if kids.tag=='x':
                                f.write(kids.text+' ')
                                # x_start=kids.text
                            elif kids.tag=='y':
                                f.write(kids.text+' ')
                                # y_start=kids.text
                            elif kids.tag=='width':
                                f.write(kids.text+' ')
                                # width_start=kids.text
                            elif kids.tag=='height':
                                f.write(kids.text+'\n')
                #                 height_start=kids.text
                # print x_start,y_start,width_start,height_start
                #
                # a12='%.6f' %(((float(x_start)+float(width_start)/2)/720))
                # a13='%.6f'%(((float(y_start)+float(height_start)/2)/576))
                # a14='%.6f'%((float(width_start)/720))
                # a15='%.6f'%((float(height_start)/576))
                # f.write('0 '+a12+' '\
                #         +a13+' '+\
                #         a14+' '\
                #         +a15+'\n')

        # for elem1 in tree.iterfind('path'):
        #     for elem2 in tree.iterfind('object/bndbox/x'):
                # for elem3 in tree.iterfind('object/bndbox/y'):
                #     for elem4 in tree.iterfind('object/bndbox/width'):
                #         for elem5 in tree.iterfind('object/bndbox/height'):
                #             print elem1.text, '1', elem2.text, elem3.text, elem4.text, elem5.text
                #             f.write(elem1.text+' 1'+' '+elem2.text+' '+elem3.text+' '+elem4.text+' '+elem5.text+'\n')