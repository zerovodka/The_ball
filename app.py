# DB 저장 (import certifi 안하면 오류남)
from pymongo import MongoClient
import certifi
ca = certifi.where()

import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

# JWT 토큰 만들 때 필요한 비밀문자열임, 아무거나 입력 가능
SECRET_KEY = 'SPARTA'

# mongoDB 연결

client = MongoClient('mongodb+srv://test:sparta@cluster0.mlula.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.miniproject

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


# HTML 주는 부분 #

# 메인 페이지
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    # 로그인한 유저일 경우
    if token_receive != None:
        try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            username = payload['id']
            return render_template('index.html', username=username)
        except jwt.ExpiredSignatureError:
            return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
        except jwt.exceptions.DecodeError:
            return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))
    # 로그인한 유저가 아닐 경우
    else:
        return render_template('index.html')


# 로그인 페이지
@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)

# 회원가입 페이지
@app.route('/register')
def register():
    msg = request.args.get("msg")
    return render_template('register.html', msg=msg)


@app.route('/user', methods=['GET'])
def user():
    # 각 사용자의 프로필과 작성 댓글 볼 수 있는
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        username = payload["id"]
        status = (username == payload["id"])  # 내 프로필이면 True, 다른 사람 프로필 페이지면 False

        user_info = db.users.find_one({"username": username}, {"_id": False})

        return render_template('user.html', user_info=user_info, status=status, username=username)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))

# 로그인 서버
@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})
    # 로그인 OK
    if result is not None:
        payload = {
         'id': username_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    # 회원가입
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,                               # 아이디
        "password": password_hash,                                  # 비밀번호
        "profile_name": username_receive,                           # 프로필 이름 기본값은 아이디
        # "profile_pic": "",                                          # 프로필 사진 파일 이름
        # "profile_pic_real": "profile_pics/profile_placeholder.png", # 프로필 사진 기본 이미지
        # "profile_info": ""                                          # 프로필 한 마디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})

# 아이디 중복확인 서버
@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})

# index_soccer_server
@app.route("/index_soccer", methods=['GET'])
def soccer():
    soccer_team_list = list(db.SOCCER.find({}, {'_id': False}))
    return jsonify({'team_list': soccer_team_list})

# index_BASKETBALL_server
@app.route("/index_basketball", methods=['GET'])
def basketball():
    basketball_team_list = list(db.BASKETBALL.find({}, {'_id': False}))
    return jsonify({'team_list': basketball_team_list})

# index_BASEBALL_server
@app.route("/index_baseball", methods=['GET'])
def baseball():
    baseball_team_list = list(db.BASEBALL.find({}, {'_id': False}))
    return jsonify({'team_list': baseball_team_list})

# index_VOLLEYBALL_server
@app.route("/index_volleyball", methods=['GET'])
def volleyball():
    volleyball_team_list = list(db.VOLLEYBALL.find({}, {'_id': False}))
    return jsonify({'team_list': volleyball_team_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


