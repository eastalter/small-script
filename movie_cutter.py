# /usr/bin/env python
# -*- coding: UTF-8 -*-

import cv2


VIDEO_PATH = 'path/to/movie'
OUT_PATH = 'path/to/folder/'
NAME = ''
video = cv2.VideoCapture(VIDEO_PATH)

flag = True
count = 0
while flag:
    print count
    end, frame = video.read()
    cv2.imwrite(OUT_PATH + NAME + str(count) + '.png', frame)
    count += 1
