import sys
#리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
from flask import Blueprint, jsonify, request
from flask import render_template
from flask import session
from flask import redirect
import pymysql as db
from DAO import VideoDAO as video
from DAO.DBConnection import dbInfo

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

@videoListController.route('/DeleteVideo/<int:cardId>', methods=['POST'])
def DeleteVideo(cardId):
    try:
        data = request.get_json()
        if not data or 'videoName' not in data:
            return jsonify({"success": False, "error": "비디오 이름을 찾을 수 없습니다."})

        videoName = data['videoName']


        connection = db.connect(
            host=dbInfo[0],
            user=dbInfo[1],
            port=dbInfo[2],
            password=dbInfo[3],
            database=dbInfo[4]
        )

        # 커서 생성
        cursor = connection.cursor()

        # video_name을 기준으로 비디오 삭제
        sql = "UPDATE videoList SET progress='delete' WHERE video_name = %s"
        cursor.execute(sql, (videoName,))
        # progress='delete'인 row를 deletedVidoe 테이블로 이동
        sql = "INSERT INTO deletedVideo SELECT * FROM videoList WHERE progress='delete'"
        # cursor.execute(sql, (progress,))
        connection.commit()
        connection.close()



        # return redirect('/videoList')
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})