import sys


from DAO.LocationDAO import GetLocation

# 리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
from flask import Blueprint, flash
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
        # 데이터베이스에서 카메라의 위치 정보 가져오기

        # return render_template('cameraMap.html', latitude=latitude, longitude=longitude)
        return render_template('cameraMap.html', location=GetLocation())

    except Exception as e:
        # 에러 핸들링 (예: 로깅, 에러 메시지 보여주기 등)
        print(f"Error occurred: {e}")  # 콘솔에 에러 메시지 출력
        return "에러발생", 500  # 사용자에게 에러 메시지 전달