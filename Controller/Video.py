from datetime import datetime, timedelta
from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
from threading import Thread
from Operation import Video
from Operation import Location

videoController = Blueprint("videoPage", __name__, url_prefix="/")

#영상 QR코드페이지 구현
@videoController.route('/QRreader')
def QRreader():
    #세션관리(세션이 없을때(로그인이 되어있지 않을때) index로 돌아감)
    if 'id' not in session:
        return redirect('/')

    #실제페이지 구현
    return render_template('QRreader.html')

#영상신청페이지 구현
@videoController.route('/videoRequest', methods=['GET', 'POST'])
def videoRequestPage():
    # 세션관리(세션이 없을때(로그인이 되어있지 않을때) index로 돌아감)
    if 'id' not in session:
        cameraID = request.args.get('cameraID', default='', type=str)
        return redirect(url_for('loginPage.loginPage', prev='videoRequest', cameraID=cameraID))

    # 실제 페이지구현
    if request.method == 'POST':
        #사용자의 위치정보수집
        latitude, longitude = request.form['location'].split(',')

        #위치정보가 카메라 부근인지 확인
        LocFlag = Location.checkLocation(request.form['cameraName'], latitude, longitude,errRange=999999)
        if LocFlag != True:
            flash("현재 카메라 주변에 없습니다. 다시 시도해주세요")
            return render_template('videoRequest.html', cameraName=request.args.get('cameraID'))


        # 페이지에 입력된 데이터 받아오기.
        data = {
            'UserId' : session['id'],
            'cameraName' : request.form['cameraName'],
            'startDay' : request.form['startDay'],
            'wantTime_s' : request.form['wantTime_s'],
            'wantTime_e' : request.form['wantTime_e'],
            'start_datetime_obj' : datetime.strptime(request.form['wantTime_s'], '%H:%M:%S'),
            'end_datetime_obj' : datetime.strptime(request.form['wantTime_e'], '%H:%M:%S'),
            'date' : int(request.form['startDay'].replace("-", "")),
            'part' : request.form['part'],
            'reason' : request.form['partText'],
            'progress' : 'in progress'
        }

        #operator 호출
        try:
            thread = Thread(target=Video.makeVideo, args=(data,))
            thread.daemon = True
            thread.start()
        except Exception as e:
            if '1062' in str(e.args):
                flash("이미 동일한 시간대의 영상을 신청하였습니다.")
            return render_template('videoRequest.html', cameraName=request.args.get('cameraID'))

        return redirect('/videoList')

    elif request.method == 'GET':
        # GET일때, 즉 사용자가 QR을 타고 접속했을때
        return render_template('videoRequest.html', cameraName=request.args.get('cameraID'))