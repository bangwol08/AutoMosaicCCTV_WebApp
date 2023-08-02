from datetime import datetime, timedelta
from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from Operation import Video

videoController = Blueprint("videoPage", __name__, url_prefix="/")

#영상신청페이지 구현
@videoController.route('/videoRequest', methods=['GET', 'POST'])
def videoRequestPage():
    # 세션관리(세션이 없을때(로그인이 되어있지 않을때) index로 돌아감)
    if 'id' not in session:
        cameraID = request.args.get('cameraID', default='', type=str)
        return redirect(url_for('loginPage.loginPage', prev='videoRequest', cameraID=cameraID))

    # 실제 페이지구현
    if request.method == 'POST':
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
            'reason' : '도난',
            'progress' : 'in progress'
        }

        #operator 호출
        try:
            Video.makeVideo(data)
        except Exception as e:
            return e

        return redirect('/videoList')

    elif request.method == 'GET':
        # GET일때, 즉 사용자가 QR을 타고 접속했을때
        return render_template('videoRequest.html', cameraName=request.args.get('cameraID'))