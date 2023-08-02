import pymysql as db
from DAO.DBConnection import dbInfo

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
        return row

    except Exception as e:
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
        return row

    except Exception as e:
        return e