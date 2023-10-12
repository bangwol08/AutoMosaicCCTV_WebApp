import sys

# 리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
from flask import Blueprint
from flask import render_template
from flask import session
from flask import redirect
from flask import request
from flask import url_for
from flask import flash
from Operation import Location
from DAO.MapDAO import GetLocation

cameraMapController = Blueprint("cameraMapPage", __name__, url_prefix="/")


@cameraMapController.route('/cameraMap', methods=['GET', 'POST'])
def cameraMap():
    # 세션관리(세션이 없을때(로그인이 되어있지 않을때) index로 돌아감)
    if 'id' not in session:
        cameraID = request.args.get('cameraID', default='', type=str)
        return redirect(url_for('loginPage.loginPage', prev='videoPage.videoRequestPage', cameraID=cameraID))
    else:
        cameraID = request.args.get('cameraID', default='', type=str)

    if request.method == 'POST':
        #사용자의 위치정보수집
        if(request.form['location'] == ''):
            latitude, longitude = 0, 0
        else:
            latitude, longitude = request.form['location'].split(',')

        #위치정보가 카메라 부근인지 확인
        LocFlag = Location.checkLocation(request.form['cameraName'], latitude, longitude,errRange=999999)
        if LocFlag != True:
            flash("현재 카메라 주변에 없습니다. 다시 시도해주세요")
            return render_template('videoRequest.html', cameraName=request.args.get('cameraID'))


    camera_location = GetLocation(cameraID)
    if camera_location:
        latitude, longitude = camera_location
    else:
        # 카메라 정보를 찾을 수 없을 경우의 처리 (예: 오류 페이지 렌더링)
        # 여기에서는 간단하게 None으로 처리합니다.
        latitude, longitude = None, None

    return render_template('cameraMap.html', latitude=latitude, longitude=longitude)
