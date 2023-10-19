import sys

from DAO import LocationDAO

# 리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
from flask import Blueprint, flash, jsonify, json, Response
from flask import render_template
from flask import session
from flask import redirect
from flask import request
from flask import url_for


cameraMapController = Blueprint("cameraMapPage", __name__, url_prefix="/")


@cameraMapController.route('/cameraMap', methods=['GET', 'POST'])
def cameraMap():

    # 세션관리(세션이 없을때(로그인이 되어있지 않을때) index로 돌아감)
    if 'id' not in session:
        cameraID = request.args.get('cameraID', default='', type=str)
        return redirect(url_for('loginPage.loginPage', prev='videoPage.videoRequestPage', cameraID=cameraID))

    try:
        cameraID = request.args.get('cameraID', default='', type=str)
          # 원하는 카메라 ID
        location_data = LocationDAO.GetLocationMap(cameraID)
        # location_data 리스트를 파이썬 딕셔너리로 변환
        location_dict = [{'latitude': item[0], 'longitude': item[1]} for item in location_data]
        # 데이터를 JSON 형식으로 직렬화
        data_json = json.dumps(location_dict)

        return render_template('cameraMap.html', data=data_json)


    except Exception as e:
        # 에러 핸들링 (예: 로깅, 에러 메시지 보여주기 등)
        print(f"Error occurred: {e}")  # 콘솔에 에러 메시지 출력
        return "에러발생", 500  # 사용자에게 에러 메시지 전달