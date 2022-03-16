import cv2
import numpy as np
nms_threshold = 0.2

thres = 0.45  # Threshold to detect object

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(10, 70)

classNames = []
classFile = 'object_detection_basic\coco.names'
with open(classFile, 'rt') as f:
    classNames = [line.rstrip() for line in f]

configPath = 'object_detection_basic\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'object_detection_basic//frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=thres)
    bbox = list(bbox)
    confs = list(np.array(confs).reshape(1, -1)[0])
    confs = list(map(float, confs))

    Indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)

    print(classIds, bbox, confs)

    if len(classIds) != 0:
        for i in Indices:
            i = i[0]
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]
            cv2.rectangle(img, (x, y), (x+w, h+y),
                          color=(0, 255, 255), thickness=2)
            cv2.putText(img, classNames[classIds[i][0]-1].upper(), (box[0]+10, box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(img, str(round(confs[i]*100, 2)), (box[0]+225, box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        # for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
        #    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
        #    cv2.putText(img, classNames[classId-1].upper(), (box[0]+10, box[1]+30),
        #                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        #    cv2.putText(img, str(round(confidence*100, 2)), (box[0]+250, box[1]+30),
        #                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Output", img)
    cv2.waitKey(1)
