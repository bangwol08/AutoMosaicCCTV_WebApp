import pymysql as db
import platform
from DAO.DBConnection import dbInfo

def InsertVideo(videoPath, videoName, sliceingCount, data):
    try:
        connection = db.connect(
            host=dbInfo[0],
            user=dbInfo[1],
            port=dbInfo[2],
            password=dbInfo[3],
            database=dbInfo[4]
        )
        # 커서 생성
        cursor = connection.cursor()
        sql = "INSERT INTO videoList (video_name, user_id, camera_id, start_day, wantTime_s, wantTime_e, part, reason, progress) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # 운영체제 감지 후 상황에 맞는 파일기본정보 및 처리상태 insert
        if platform.system() == 'Windows':
            cursor.execute(sql, (
            f'{videoPath[sliceingCount:]}{videoName}', data['UserId'], data['cameraName'], data['startDay'], data['wantTime_s'], data['wantTime_e'], data['part'],
            data['reason'], data['progress']))
        elif platform.system() == 'Linux':
            cursor.execute(sql, (
            f'{videoPath[sliceingCount:]}{videoName}_h264.mp4', data['UserId'], data['cameraName'], data['startDay'], data['wantTime_s'], data['wantTime_e'], data['part'],
            data['reason'], data['progress']))

        connection.commit()
        connection.close()

    except Exception as e:
        connection.close()
        raise e

def UpdateVideo_Err(videoPath, videoName, sliceingCount, UserId):
    try:
        connection = db.connect(
            host=dbInfo[0],
            user=dbInfo[1],
            port=dbInfo[2],
            password=dbInfo[3],
            database=dbInfo[4]
        )
        # 커서 생성
        cursor = connection.cursor()
        # update문 작성
        sql = "UPDATE videoList SET progress=%s WHERE video_name=%s AND user_id=%s"

        # 운영체제 감지 후 그에 맞는 쿼리 문 실행
        if platform.system() == 'Windows':
            cursor.execute(sql, ('error', f'{videoPath[sliceingCount]}{videoName}', UserId))
        elif platform.system() == 'Linux':
            cursor.execute(sql, ('error', f'{videoPath[sliceingCount]}{videoName}_h264.mp4', UserId))

        connection.commit()
        connection.close()
    except Exception as e:
        connection.close()
        raise e

def UpdateVideo_Com(videoPath, videoName, sliceingCount, UserId):
    try:
        connection = db.connect(
            host=dbInfo[0],
            user=dbInfo[1],
            port=dbInfo[2],
            password=dbInfo[3],
            database=dbInfo[4]
        )
        # 커서 생성
        cursor = connection.cursor()
        # update문 작성
        sql = "UPDATE videoList SET progress=%s WHERE video_name=%s AND user_id=%s"

        # 운영체제 감지 후 그에 맞는 쿼리 문 실행
        if platform.system() == 'Windows':
            cursor.execute(sql, ('complete', f'{videoPath[sliceingCount:]}{videoName}', UserId))
        elif platform.system() == 'Linux':
            cursor.execute(sql, ('complete', f'{videoPath[sliceingCount:]}{videoName}_h264.mp4', UserId))

        connection.commit()
        connection.close()
    except Exception as e:
        connection.close()
        raise e

# videoList
def getListRow(id):
    try:
        # dbInfo = DBConnection.dbInfo
        connection = db.connect(
            host=dbInfo[0],
            user=dbInfo[1],
            port=dbInfo[2],
            password=dbInfo[3],
            database=dbInfo[4]
        )
        cursor = connection.cursor()
        sql = "SELECT count(*) FROM videoList WHERE user_id=%s"
        cursor.execute(sql, (id))
        row = cursor.fetchone()
        connection.close()
        return row

    except Exception as e:
        connection.close()
        return e

def getList(id):
    try:
        # dbInfo = DBConnection.dbInfo
        connection = db.connect(
            host=dbInfo[0],
            user=dbInfo[1],
            port=dbInfo[2],
            password=dbInfo[3],
            database=dbInfo[4]
        )
        cursor = connection.cursor()
        sql = "SELECT * FROM videoList WHERE user_id=%s"
        cursor.execute(sql, (id))
        row = cursor.fetchall()
        connection.close()
        return row

    except Exception as e:
        connection.close()
        return e