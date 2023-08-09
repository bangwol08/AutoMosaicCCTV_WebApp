from flask import Flask
from . import Login, Video
from . import Index
from . import videoList

app = Flask(__name__)

#메인페이지 관련 페이지
app.register_blueprint(Index.indexController)

#로그인/로그아웃 기능 관련 페이지
app.register_blueprint(Login.loginController)

#영상목록 기능 관련 페이지
app.register_blueprint(videoList.videoListController)

# QR 및 리퀘스트 기능 관련 페이지
app.register_blueprint(Video.videoController)


