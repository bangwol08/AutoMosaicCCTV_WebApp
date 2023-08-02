import pymysql as db
import hashlib
from DAO.DBConnection import dbInfo

def SelectUser(id,pw):
    try:
        connection = db.connect(
            host=dbInfo[0],
            user=dbInfo[1],
            port=dbInfo[2],
            password=dbInfo[3],
            database=dbInfo[4]
        )
        pwhash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
        cursor = connection.cursor()
        sql = "SELECT id, name FROM login WHERE id=%s AND password=%s"
        cursor.execute(sql, (id, pwhash))
        row = cursor.fetchone()
        return row

    except Exception as e:
        raise e