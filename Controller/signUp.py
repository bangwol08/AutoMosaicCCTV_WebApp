from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import flash
from flask import redirect
from flask import url_for
from Operation import Sign
from flask import jsonify

SignUpController = Blueprint("signupPage", __name__, url_prefix="/")

# 로그인 페이지
@SignUpController.route('/signup', methods=['GET', 'POST'])
def signupPage():
    return render_template('signUp.html')

@SignUpController.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        try:
            id = request.form.get('id')
            password = request.form.get('password')
            passcheck = request.form.get('passcheck')
            name = request.form.get('name')
            age = request.form.get('age')
            gender = request.form.get('gender')
            phonenum = request.form.get('phonenum')
            email = request.form.get('email')
            address = request.form.get('address')
            aggrement = request.form.get('aggrement')
            row = Sign.signUp(id, password, passcheck, name, age, gender, phonenum, email, address, aggrement)
            if row is 1:
                flash("이미 있는 아이디입니다. 다시 가입해주세요.")
                return redirect('/signup')
            else:
                return render_template("regist.html")
        except:
            flash("회원가입 실패")
            return redirect("/signup")
    else :
        return render_template('signUp.html')