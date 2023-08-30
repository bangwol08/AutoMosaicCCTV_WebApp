import sys
#리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
from DAO import SignDAO

def signUp(id, password, passcheck, name, age, gender, phonenum, email, address, aggrement):
    try:
        row = SignDAO.servicesign(id)
        if row is not None:
            return 1
        else:
            row = SignDAO.signUp(id, password, passcheck, name, age, gender, phonenum, email, address, aggrement)
            return row
    except Exception as e:
        raise e