from flask import Flask
from . import Login, Video, CameraMap
from . import Index
from . import videoList
from . import signUp
from . import Uplodad

app = Flask(__name__)

#메인페이지 관련 페이지
app.register_blueprint(Index.indexController)

#회원가입 기능 관련 페이지
app.register_blueprint(signUp.SignUpController)

#로그인/로그아웃 기능 관련 페이지
app.register_blueprint(Login.loginController)

#영상목록 기능 관련 페이지
app.register_blueprint(videoList.videoListController)

# QR 및 리퀘스트 기능 관련 페이지
app.register_blueprint(Video.videoController)

# 프레임업로드
app.register_blueprint(Uplodad.upload)

# 카메라맵 페이지
app.register_blueprint(CameraMap.cameraMapPageController)
