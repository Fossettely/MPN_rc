import os
import numpy as np
import cv2

"将上海数据集视频转帧 "

video_src_path = 'data/training/videos/' #数据集路径
label_name = os.listdir(video_src_path)
label_dir = {}
index = 0
videos = os.listdir(video_src_path)
# 过滤出avi文件
videos = filter(lambda x: x.endswith('avi'), videos)
for each_video in videos:
    each_video_name = each_video.split('.')[-2]
    # print(video_name)
    # each video save path
    video_save_path = os.path.join(video_src_path, each_video_name)
    if not os.path.exists(video_save_path):
        os.mkdir(video_save_path)
    print(video_save_path)
    # each read aiv name
    each_video_fullname = video_src_path + each_video
    print(each_video_fullname)
    cap = cv2.VideoCapture(each_video_fullname)
    success = True
    frame_count = 1
    while success:
        success, frame = cap.read()
    
        params = []
        params.append(1)
        if success:
            cv2.imwrite(video_save_path + '/' + str(frame_count) + '.jpg', frame, params)

            frame_count += 1
            if frame is None:
                frame_count = 1
                continue
    cap.release()

