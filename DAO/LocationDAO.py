import pymysql as db
from DAO.DBConnection import dbInfo
def GetLocationMap(cameraID):
    try:
        connection = db.connect(
            host=dbInfo[0],
            user=dbInfo[1],
            port=dbInfo[2],
            password=dbInfo[3],
            database=dbInfo[4]
        )
        cursor = connection.cursor()
        sql = "SELECT latitude, longitude FROM camera WHERE camera_id=%s"
        cursor.execute(sql, (cameraID))
        data = cursor.fetchall()
        connection.close()
        return data

    except Exception as e:
        connection.close()
        raise e