import pymysql as db
import hashlib
from DAO.DBConnection import dbInfo

def servicesign(id):
    try:
        connection = db.connect(
            host=dbInfo[0],
            user=dbInfo[1],
            port=dbInfo[2],
            password=dbInfo[3],
            database=dbInfo[4]
        )
        cursor = connection.cursor()
        sql = "SELECT id FROM login WHERE id=%s"
        cursor.execute(sql, (id))
        row = cursor.fetchone()
        connection.close()
        return row

    except Exception as e:
        connection.close()
        raise e

def signUp(id, password, passcheck, name, age, gender, phonenum, email, address, aggrement):
    connection = db.connect(
        host=dbInfo[0],
        user=dbInfo[1],
        port=dbInfo[2],
        password=dbInfo[3],
        database=dbInfo[4]
    )
    hashpass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor = connection.cursor()
    sql = "insert into login (id, password, name, age, gender, phonenum, email, address, aggrement) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (id, hashpass, name, age, gender, phonenum, email, address, aggrement))
    connection.commit()
    row = cursor.fetchone()
    connection.close()
    return row