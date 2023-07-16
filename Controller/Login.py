from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import flash
from flask import redirect
from flask import url_for
from Operation import User

loginController = Blueprint("loginPage", __name__, url_prefix="/")

# 로그인 페이지
@loginController.route('/login', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        try:
            User.login(request.form['user'], request.form['pwd'])
            #이전페이지 감지 후 페이지로 이동
            if request.form['prev'] != 'None' and request.form['cameraID'] != 'None':
                return redirect(url_for(request.form['prev'], cameraID=request.form['cameraID']))
            else:
                return redirect('/')
        except:
            flash("아이디 또는 비밀번호가 틀렸습니다. 다시 확인해주세요.")
            return render_template('login.html', prev=request.form['prev'], cameraID=request.form['cameraID'])
    else:
        return render_template('login.html', prev=request.args.get('prev'), cameraID=request.args.get('cameraID'))

# 로그아웃 페이지
@loginController.route('/logout')
def logoutPage():
    # 세션관리(세션이 없을때(로그인이 되어있지 않을때) index로 돌아감)
    if 'id' not in session:
        return redirect('/')

    # 실제 페이지구현
    User.logout()
    return redirect('/')