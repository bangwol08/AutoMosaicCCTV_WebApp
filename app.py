import sys
#리눅스를 위한 경로추가
sys.path.append('/home/hosting/WebApp')
from Controller import app
from datetime import timedelta
########작성금지#############
app.config["SECRET_KEY"] = "sh291hfwnh8@hwqjh2(*@#*Uh2N2920hF@H0Fh@C293"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)