# import sys
# sys.path.insert(0,'/home/scw4750/caffe-master/python')

import caffe
import numpy as np

net=caffe.Net('H:/LightCNN/deploy_C.prototxt','H:/LightCNN/LightenedCNN_C.caffemodel',caffe.TEST)
params=['conv1','conv2a','conv2','conv3a','conv3','conv4a','conv4','conv5a','conv5','fc1','fc2']
# net_params={pr: (net.params[pr][0].data, net.params[pr][1].data) for pr in params}

face_net=caffe.Net('H:/LightCNN/face_C.prototxt','H:/LightCNN/LightenedCNN_C.caffemodel',caffe.TEST)
face=['face_conv1','face_conv2a','face_conv2','face_conv3a','face_conv3','face_conv4a','face_conv4','face_conv5a','face_conv5','face_fc1','face_fc2']
# face_params={face_pr: (face_net.params[face_pr][0].data, face_net.params[face_pr][1].data) for face_pr in face}

for pr, face_pr in zip(params,face):
    face_net.params[face_pr][0].data[...] = net.params[pr][0].data
    face_net.params[face_pr][1].data[...] = net.params[pr][1].data
face_net.save('H:/Face_LightCNN.caffemodel')
