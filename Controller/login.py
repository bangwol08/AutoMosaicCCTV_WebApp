from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import flash
from flask import redirect
from flask import url_for
from DAO import UserDAO

loginPage = Blueprint("loginPage", __name__, url_prefix="/")

# 로그인 페이지
@loginPage.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = UserDAO
        row = user.SelectUser(request.form['user'], request.form['pwd'])
        if row is not None:
            # 로그인 성공
            session['id'] = row[0]
            session['name'] = row[1]
            print(request.form['prev'])
            if request.form['prev'] != 'None' and request.form['cameraID'] != 'None':
                return redirect(url_for(request.form['prev'], cameraID=request.form['cameraID']))
            else:
                return redirect('/')
        else:
            # 로그인 실패
            flash("아이디 또는 비밀번호가 틀렸습니다. 다시 확인해주세요.")
            return render_template('login.html', prev=request.form['prev'], cameraID=request.form['cameraID'])
    else:
        return render_template('login.html', prev=request.args.get('prev'), cameraID=request.args.get('cameraID'))