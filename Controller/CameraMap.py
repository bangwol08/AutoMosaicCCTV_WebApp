import sys

# 리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
from flask import Blueprint
from flask import render_template
from flask import session
from flask import redirect

cameraMapPageController = Blueprint("cameraMapPage", __name__, url_prefix="/")


@cameraMapPageController.route('/cameraMap')
def cameraMap():
    # 세션관리(세션이 없을때(로그인이 되어있지 않을때) index로 돌아감)
    if 'id' not in session:
        return redirect('/')

    return render_template('cameraMap.html')
