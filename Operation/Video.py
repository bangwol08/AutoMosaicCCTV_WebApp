import platform
import os
import threading

import cv2
import glob
from datetime import datetime, timedelta
from DAO import VideoDAO

def makeVideo(data):
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

        out1 = cv2.VideoWriter(f'{videoPath}{videoName}', fourcc2, 8.0, (640, 480))

        # 각 폴더 내의 모든 이미지를 읽어와서 비디오에 추가
        for folder in folder_paths:
            images = sorted(glob.glob(f'{folder}/*'))  # 각 폴더 내의 .jpg 파일들을 정렬하여 가져옴
            for image in images:
                frame = cv2.imread(image)
                out1.write(frame)  # 프레임을 비디오에 추가

        # VideoWriter 객체 닫기
        out1.release()

        # 운영체제 감지 후 리눅스일시 ffmpeg로 h264로 영상변환
        if platform.system() == 'Linux':
            os.system(
                f"ffmpeg -i /home/hosting/WebApp/Controller/static/video/{data['UserId']}/{videoName} -vcodec libx264 /home/hosting/WebApp/Controller/static/video/{data['UserId']}/{videoName}_h264.mp4")

        #완료 후 complete상태 업데이트
        VideoDAO.UpdateVideo_Com(videoPath, videoName, sliceingCount, data['UserId'])

    except Exception as e:
        #에러시 err상태 업데이트 및 out1 release
        VideoDAO.UpdateVideo_Err(videoPath, videoName, sliceingCount, data['UserId'])
        out1.release()