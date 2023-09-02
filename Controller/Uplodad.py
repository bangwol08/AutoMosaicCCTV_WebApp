import sys
#리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
import os
import platform
from flask import Blueprint
from flask import request
from datetime import datetime

upload = Blueprint("upload", __name__, url_prefix="/")

@upload.route('/camera/original', methods=['GET', 'POST'])
def OriginalUpload():
    #필요한 데이터 받아오기
    file = request.files['frame']
    timeStamp = datetime.fromtimestamp(float(request.form.get('time')))
    cameraID = request.form.get('cameraID')
    day_form = timeStamp.strftime('%Y%m%d')
    time_form = timeStamp.strftime('%H%M')
    micro_form = timeStamp.strftime('%S%f')

    #필요한 데이터 가공하기
    if platform.system() == 'Windows':
        dirName = f'./Controller/static/uploads/{cameraID}/original/{day_form}/{time_form}'
        fileName = f'{micro_form}.jpg'
    elif platform.system() == 'Linux':
        dirName = f'./WebApp/Controller/static/uploads/{cameraID}/original/{day_form}/{time_form}'
        fileName = f'{micro_form}.jpg'

    #디렉토리 존재여부 확인
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        file.save(f'{dirName}/{fileName}')
    else:
        file.save(f'{dirName}/{fileName}')

    return "1"

@upload.route('/camera/process', methods=['GET', 'POST'])
def ProcessUpload():
    # 필요한 데이터 받아오기
    file = request.files['frame']
    timeStamp = datetime.fromtimestamp(float(request.form.get('time')))
    cameraID = request.form.get('cameraID')
    day_form = timeStamp.strftime('%Y%m%d')
    time_form = timeStamp.strftime('%H%M')
    micro_form = timeStamp.strftime('%S%f')

    # 필요한 데이터 가공하기
    if platform.system() == 'Windows':
        dirName = f'./Controller/static/uploads/{cameraID}/process/{day_form}/{time_form}'
        fileName = f'{micro_form}.jpg'
    elif platform.system() == 'Linux':
        dirName = f'./WebApp/Controller/static/uploads/{cameraID}/process/{day_form}/{time_form}'
        fileName = f'{micro_form}.jpg'

    # 디렉토리 존재여부 확인
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        file.save(f'{dirName}/{fileName}')
    else:
        file.save(f'{dirName}/{fileName}')

    return "1"