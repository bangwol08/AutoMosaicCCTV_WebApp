from flask import session
from DAO import UserDAO
def login(id,pw):
    try:
        row = UserDAO.SelectUser(id,pw)

        if row is not None:
            # 로그인 성공
            session['id'] = id
            session['name'] = pw
        else:
            # 로그인 실패
            raise Exception
    except Exception as e:
        raise e

def logout():
    session.clear()
    session.modified = True