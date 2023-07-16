from flask import Blueprint
from flask import render_template

indexController = Blueprint("indexPage", __name__, url_prefix="/")

# 로그인 페이지
@indexController.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')