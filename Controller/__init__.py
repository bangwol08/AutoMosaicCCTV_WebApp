from flask import Flask
from . import Login
from . import Index
from . import videoList

app = Flask(__name__)

#메인페이지 관련 페이지
app.register_blueprint(Index.indexController)

#로그인/로그아웃 기능 관련 페이지
app.register_blueprint(Login.loginController)

#영상관련 기능 관련 페이지
app.register_blueprint(videoList.videoListController)
