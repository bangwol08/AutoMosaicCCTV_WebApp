import sys
#리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
from DAO import UserDAO

def login(id,pw):
    try:
        row = UserDAO.SelectUser(id,pw)

        if row is not None:
            # 로그인 성공
            return row[0], row[1]
        else:
            # 로그인 실패
            raise Exception
    except Exception as e:
        raise e