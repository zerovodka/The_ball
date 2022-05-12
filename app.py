import hashlib
import jwt as jwt
import certifi

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.g1o5l.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta_plus_week1

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 비밀 키 설정
SECRET_KEY = 'SPARTA'

from datetime import datetime, timedelta


# 메인 페이지 이동
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    if token_receive is not None:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)
        user_info = db.users.find_one({"id": payload["id"]})
        print(user_info)
        login_status = 1
        return render_template('index.html', user_info=user_info, login_status=login_status)
    else:
        login_status = 0
        return render_template('index.html', login_status=login_status)


# 로그인 페이지 이동
@app.route('/login')
def login():
    return render_template('login.html')


# 회원 가입 페이지 이동
@app.route('/signup')
def signup():
    return render_template('signup.html')


# # 각 스포츠 페이지 이동
# 밑에 크롤링 함수랑 중복돼서 에러남 -> 주석 처리
# @app.route('/soccer_team')
# def soccer_team():
#     token_receive = request.cookies.get('mytoken')
#     if token_receive is not None:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         print(payload)
#         user_info = db.users.find_one({"id": payload["id"]})
#         print(user_info)
#         login_status = 1
#         return render_template('.html', user_info=user_info, login_status=login_status)
#     else:
#         login_status = 0
#         return render_template('soccer.html', login_status=login_status)
#
#
# @app.route('/baseball')
# def baseball():
#     return render_template('baseball.html')
#
#
# @app.route('/basketball')
# def basketball():
#     return render_template('basketball.html')
#
#
# @app.route('/valleyball')
# def valleyball():
#     return render_template('valleyball.html')


# 댓글 게시판 이동
@app.route('/comment')
def comment():
    token_receive = request.cookies.get('mytoken')
    if token_receive is not None:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # print(payload)
        user_info = db.users.find_one({"id": payload["id"]})
        # print(user_info)
        login_status = 1
        return render_template('comment.html', user_info=user_info, login_status=login_status)
    else:
        login_status = 0
        return render_template('comment.html', login_status=login_status)


# 댓글 저장
@app.route('/posting', methods=['POST'])
def posting():
    token_recieve = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_recieve, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"id": payload["id"]})
        comment_recieve = request.form["comment_give"]
        date_recieve = request.form["date_give"]

        doc = {
            'username': user_info['id'],
            'comment': comment_recieve,
            'date': date_recieve
        }
        db.posts.insert_one(doc)
        return jsonify({'result': 'success', 'msg': '응원 작성 완료!'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return render_template('index.html')


# 댓글 가져오기
@app.route('/get_posts', methods=['GET'])
def get_posts():
    token_recieve = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_recieve, SECRET_KEY, algorithms=['HS256'])
        posts = list(db.posts.find({}).sort('date', -1).limit(20))

        # 추후 좋아요 넣었을 때 어느 포스트인지 구별하기 위해
        for post in posts:
            post['_id'] = str(post['_id'])
            post["count_heart"] = db.likes.count_documents({"post_id": post["_id"], "type": "heart"})
            post["heart_by_me"] = bool(
                db.likes.find_one({"post_id": post["_id"], "type": "heart", "username": payload['id']}))

        return jsonify({'result': 'success', 'msg': '최신화!', 'posts': posts})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return render_template('index.html')


# 로그인 API
@app.route('/sign_in', methods=['POST'])
def sign_in():
    id_receive = request.form['give_id']
    pw_receive = request.form['give_pw']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')
                             ).hexdigest()  # 패스워드 암호화

    result = db.users.find_one(
        {'id': id_receive, 'pw': pw_hash})  # 동일한 유저가 있는지 확인

    if result is not None:  # 동일한 유저가 없는게 아니면, = 동일한 유저가 있으면,
        payload = {
            'id': id_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
        }

        token = jwt.encode(payload, SECRET_KEY,
                           algorithm='HS256')  # .decode('utf8')
        # .decode('utf8')  # 토큰을 건내줌.
        return jsonify({'result': 'success', 'token': token, 'msg': '환영합니다.'})
        # return jsonify({'result': 'success', 'token': str(token), 'msg': '환영합니다.'})
    else:  # 동일한 유저가 없으면,
        return jsonify({'result': 'fail', 'msg': '아이디/패스워드가 일치하지 않습니다.'})


# 회원가입 API
@app.route("/users_signup", methods=["POST"])
def users():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    # name_receive = request.form['name_give']
    # email_receive = request.form['email_give']
    # address_receive = request.form['address_give']

    # Encrypt
    pw_encode = pw_receive.encode()
    pw_hash = hashlib.sha256(pw_encode).hexdigest()

    doc = {
        'id': id_receive,
        'pw': pw_hash
        # 'name': name_receive,
        # 'email': email_receive,
        # 'address': address_receive
    }
    db.users.insert_one(doc)

    return jsonify({'msg': '회원 가입 완료!'})


# 아이디 중복 확인 API
@app.route("/users_idCheck", methods=["GET"])
def getId():
    id_receive = request.values.get('id_give')
    user = db.users.find_one({'id': id_receive})
    if user is None:  # datatype 이 none일경우 []를 통한 접근 불가 ex) user is None <- ok but, user['id'] is None <- 데이터 타입 오류
        return jsonify({'user': True})
    else:
        return jsonify({'user': False})


# 좋아요 API
@app.route('/update_like', methods=['POST'])
def update_like():
    token_recieve = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_recieve, SECRET_KEY, algorithms=['HS256'])

        user_info = db.users.find_one({"id": payload["id"]})
        post_id_receive = request.form["post_id_give"]
        type_receive = request.form["type_give"]
        action_receive = request.form["action_give"]

        doc = {
            "post_id": post_id_receive,
            'username': user_info['id'],
            "type": type_receive
        }

        if action_receive == "like":
            db.likes.insert_one(doc)
        else:
            db.likes.delete_one(doc)

        count = db.likes.count_documents({"post_id": post_id_receive, "type": type_receive})

        return jsonify({"result": "success", 'msg': 'updated', "count": count})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return render_template('index.html')


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
