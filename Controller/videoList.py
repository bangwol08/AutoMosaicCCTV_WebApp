from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import flash
from flask import redirect
from flask import url_for
from Operation import User

videoListController = Blueprint("videoListPage", __name__, url_prefix="/")

@videoListController.route('/videoList')
def videoList():
    # 세션관리(세션이 없을때(로그인이 되어있지 않을때) index로 돌아감)
    if 'id' not in session:
        return redirect('/')

        # request받으면 영상을 videoList에 업로드 할 수 있도록 (로딩바)

    # 실제 페이지구현
    listRow = video.getListRow(session['id'])
    list = video.getList(session['id'])

    return render_template('videoList.html', listRow=listRow[0], list=list)