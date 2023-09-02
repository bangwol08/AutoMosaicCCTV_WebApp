import datetime
import os
import platform
import sys
#리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
from flask import Blueprint, jsonify, request
from flask import render_template
from flask import session
from flask import redirect
import pymysql as db
from DAO import VideoDAO as video, VideoDAO
from DAO.DBConnection import dbInfo

videoListController = Blueprint("videoListPage", __name__, url_prefix="/")

@videoListController.route('/videoList')
def videoList():
    # 세션관리(세션이 없을때(로그인이 되어있지 않을때) index로 돌아감)
    if 'id' not in session:
        return redirect('/')

        # request받으면 영상을 videoList에dudf 업로드 할 수 있도록 (로딩바)

    # 실제 페이지구현
    listRow = video.getListRow(session['id'])
    list = video.getList(session['id'])

    return render_template('videoList.html', listRow=listRow[0], list=list)


@videoListController.route('/deleteUpdate', methods=['POST'])
def deleteUpdate():
    try:
        data = request.get_json()
        videoName = data['videoName']


        if platform.system() == 'Windows':
            videoPath = f"./Controller/static/video/{data['UserId']}/"
            videoName = f"{data['cameraName']}_{datetime.strftime(data['start_datetime_obj'], '%H_%M_%S')}_{datetime.strftime(data['end_datetime_obj'], '%H_%M_%S')}.mp4"
            sliceingCount = 20
        elif platform.system() == 'Linux':
            videoPath = f"./WebApp/Controller/static/video/{data['UserId']}/"
            videoName = f"{data['cameraName']}_{datetime.strftime(data['start_datetime_obj'], '%H_%M_%S')}_{datetime.strftime(data['end_datetime_obj'], '%H_%M_%S')}.mp4"
            sliceingCount = 27

        # 비디오의 초기상태 Insert(신청자 정보, 진행상황=Progress 등)
        VideoDAO.InsertVideo(videoPath, videoName, sliceingCount, data)

        fullVideoPath = os.path.join(videoPath, videoName)

        if os.path.exists(fullVideoPath):
            os.remove(fullVideoPath)
            print('비디오 파일 삭제 성공')
        else:
            print('삭제할 비디오 파일이 존재하지 않습니다.')

        # 완료 후 delete상태 업데이트
        VideoDAO.UpdateVideo_Del(videoName, data['UserId'])
    # except Exception as e:
    #     print('비디오 파일 삭제 실패:', e)
        return jsonify({"success": True})

    except Exception as e:
        print('비디오 파일 삭제 실패:', e)
        return jsonify({"success": False, "error": str(e)})


# 원본
# @videoListController.route('/DeleteVideo/<int:cardId>', methods=['POST'])
# def DeleteVideo(cardId):
#     try:
#         data = request.get_json()
#         if not data or 'videoName' not in data:
#             return jsonify({"success": False, "error": "비디오 이름을 찾을 수 없습니다."})
#
#         videoName = data['videoName']
#         UserId = data['UserId']
#
#         connection = db.connect(
#             host=dbInfo[0],
#             user=dbInfo[1],
#             port=dbInfo[2],
#             password=dbInfo[3],
#             database=dbInfo[4]
#         )
#
#         # 커서 생성
#         cursor = connection.cursor()
#
#         # video_name을 기준으로 비디오 삭제
#         sql_delete = "DELETE FROM videoList WHERE video_name = %s"
#         cursor.execute(sql_delete, (videoName,))
#         connection.commit()
#         connection.close()
#
#         return jsonify({"success": True})
#
#     except Exception as e:
#         return jsonify({"success": False, "error": str(e)})