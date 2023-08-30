import sys
#리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
from DAO import CameraDAO
import decimal

def checkLocation(cameraID,latitude, longitude,errRange):
    row = CameraDAO.SelectCamera(cameraID)

    if row == None:
        return False

    if decimal.Decimal(row[0]) - errRange <= decimal.Decimal(latitude) <= decimal.Decimal(row[0]) + errRange:
        if decimal.Decimal(row[1]) - errRange <= decimal.Decimal(longitude) <= decimal.Decimal(row[1]) + errRange:
            return True
        else:
            # return False
            return True
    else:
        # return False
        return True