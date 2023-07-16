from flask import session
from DAO import UserDAO
def login(id,pw):
    row = UserDAO.SelectUser(id,pw)

    if row is not None:
        # 로그인 성공
        return id, pw
    else:
        # 로그인 실패
        raise Exception

def logout():
    session.clear()
    session.modified = True