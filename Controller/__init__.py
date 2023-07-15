from flask import Flask
from . import login
from . import index

app = Flask(__name__)

#메인페이지 관련 페이지
app.register_blueprint(index.indexPage)

#로그인/로그아웃 기능 관련 페이지
app.register_blueprint(login.loginPage)
