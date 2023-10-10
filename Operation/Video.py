import sys
#리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
import platform
import glob
from datetime import datetime, timedelta
import cv2
from ultralytics import YOLO
import os
from DAO import VideoDAO
import time

yolo_model = YOLO('yolov8n.pt')
def yolo_process(frame):
    output = frame.copy()
    outs = yolo_model(output, classes=0, conf=0.3)
    boxes = []

    for see in outs:
        for detection in see:  # see == outs[0,1,2,3 ..., n]
            boxes_buf = detection.boxes  #
            box = boxes_buf[0]  # 가장 높은 conf 값을 갖은 것
            x, y, w, h = box.xywh[0].tolist()
            boxes.append([x, y, w, h])

    for i in range(len(boxes)):
        if i < len(boxes):
            x, y, w, h = boxes[i]
            x, y, w, h = int(x), int(y), int(w), int(h)
            x1 = x - w // 2
            x2 = x + w // 2
            y1 = y - h // 2
            y2 = y + h // 2
            # reduce the y2 coordinate by 20% of the original height
            y2_new = int(y1 + (y2 - y1) * 0.3)
            # reduce the x2 coordinate by 50% of the original width
            # x2_new = int(x1 + (x2 - x1) / 4 * 3)
            x2_new = int(x2 - (x2 - x1) / 4)
            # increase the x1 coordinate by 50% of the original width
            x1_new = int(x1 + (x2 - x1) / 4)

            # print(f'x = {x}, {type(x)}, y = {y}, {type(y)}, w = {w}, {type(w)}, h = {h}, {type(h)}')
            region = output[y1:y2_new, x1_new: x2_new]
            height, width = region.shape[:2]
            w = int(width * 0.1)
            h = int(height * 0.1)
            if w <= 0:
                w = 1
            if h <= 0:
                h = 1

            small = cv2.resize(region, (w, h), interpolation=cv2.INTER_AREA)
            mosaic = cv2.resize(small, (width, height), interpolation=cv2.INTER_NEAREST)
            output[y1:y2_new, x1_new:x2_new] = mosaic
    return output
def makeVideo(data):
    startTime = time.time()
    # 운영체제 감지 후 영상 저장 경로 지정
    if platform.system() == 'Windows':
        videoPath = f"./Controller/static/video/{data['UserId']}/"
        videoName = f"{data['cameraName']}_{datetime.strftime(data['start_datetime_obj'], '%H_%M_%S')}_{datetime.strftime(data['end_datetime_obj'], '%H_%M_%S')}.mp4"
        folder_dir = f"./Controller/static/uploads/{data['cameraName']}/process/{data['date']}/"  # 프레임 경로
        sliceingCount = 20
    elif platform.system() == 'Linux':
        videoPath = f"./WebApp/Controller/static/video/{data['UserId']}/"
        videoName = f"{data['cameraName']}_{datetime.strftime(data['start_datetime_obj'], '%H_%M_%S')}_{datetime.strftime(data['end_datetime_obj'], '%H_%M_%S')}.mp4"
        folder_dir = f"./WebApp/Controller/static/uploads/{data['cameraName']}/process/{data['date']}/"  # 프레임 경로
        sliceingCount = 27

    #비디오의 초기상태 Insert(신청자 정보, 진행상황=Progress 등)
    VideoDAO.InsertVideo(videoPath, videoName, sliceingCount, data)

    # 지정디렉토리가 없을시 디렉토리 생성
    if not os.path.exists(f'{videoPath}'):
        os.makedirs(f'{videoPath}')

    # 프레임 -> 영상전환 코드
    try:
        folder_paths = []
        mintime = 0

        # 시간 범위 내의 모든 폴더 경로를 가져옴
        while True:
            compareTime = data['start_datetime_obj'] + timedelta(minutes=mintime)
            if compareTime <= data['end_datetime_obj']:
                folder_paths.append(f'{folder_dir}{compareTime.hour:02d}{compareTime.minute:02d}')
            else:
                break
            mintime = mintime + 1

         # 운영체제 감지 후 상황에 맞는 코덱 설정
        if platform.system() == 'Windows':
            # 웹 브라우저용 코덱 : h264 or x264  avc1'
            fourcc2 = cv2.VideoWriter_fourcc(*'h264')
        elif platform.system() == 'Linux':
            fourcc2 = cv2.VideoWriter_fourcc(*'mp4v')

        out1 = cv2.VideoWriter(f'{videoPath}{videoName}', fourcc2, 30.0, (640, 480))

        # 각 폴더 내의 모든 이미지를 읽어와서 비디오에 추가
        for folder in folder_paths:
            images = sorted(glob.glob(f'{folder}/*'))  # 각 폴더 내의 .jpg 파일들을 정렬하여 가져옴
            for image in images:
                frame = yolo_process(cv2.imread(image))
                out1.write(frame)  # 프레임을 비디오에 추가

        # VideoWriter 객체 닫기
        out1.release()

        # 운영체제 감지 후 리눅스일시 ffmpeg로 h264로 영상변환
        if platform.system() == 'Linux':
            os.system(
                f"ffmpeg -i /home/hosting/WebApp/Controller/static/video/{data['UserId']}/{videoName} -vcodec libx264 /home/hosting/WebApp/Controller/static/video/{data['UserId']}/{videoName}_h264.mp4")

        #완료 후 complete상태 업데이트
        VideoDAO.UpdateVideo_Com(videoPath, videoName, sliceingCount, data['UserId'])
        endTime = time.time()

        print(endTime - startTime)
    except:
        #에러시 err상태 업데이트 및 out1 release
        VideoDAO.UpdateVideo_Err(videoPath, videoName, sliceingCount, data['UserId'])
        out1.release()