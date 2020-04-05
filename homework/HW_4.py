from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('HW_4.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
   # 1. 클라이언트가 준 title, author, review 가져오기.
   name = request.form['name']
   count = request.form['count']
   address = request.form['address']
   phone = request.form['phone']

   # 2. DB에 정보 삽입하기
   doc = {
      'name' : name,
      'count' : count,
      'address' : address,
      'phone' : phone
   }

   print(doc)

   db.orders.insert_one(doc)

   # 3. 성공 여부 & 성공 메시지 반환하기

   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route('/orders', methods=['GET'])
def read_orders():
   # 1. 모든 reviews의 문서를 가져온 후 list로 변환합니다.
   orders = list(db.orders.find({},{"_id":0}))

   # 2. 성공 메시지와 함께 리뷰를 보냅니다.
   return jsonify({'result':'success', 'msg': '이 요청은 GET!','orders':orders})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
