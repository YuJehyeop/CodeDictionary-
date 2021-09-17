from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework

## HTML 화면 보여주기
def home():
   return render_template('index.html')

# POST API 기본 코드
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']  # 'title_give'로 가져온값 읽어줘봐
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

# GET(Read) API 기본코드
@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')  # 'title_give'로 가져온값 읽어줘봐
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


# html 소스
<script type="text/javascript">

            $(document).ready(function () {
                showReview();
            });

            # POST요청 확인 Ajax 기본코드
            function makeReview() {
                $.ajax({
                    type: "POST",
                    url: "/review",
                    data: {sample_give:'샘플데이터'},
                    success: function (response) {
                        alert(response["msg"]);
                        window.location.reload();
                    }
                })
            }
            # GET요청 확인 Ajax 코드
            function showReview() {
                $.ajax({
                    type: "GET",
                    url: "/review?sample_give=샘플데이터",
                    data: {},
                    success: function (response) {
                        alert(response["msg"]);
                    }
                })
            }
        </script>

# ------------------------------------------------------------------------------------------



# 작업 예시  app
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name_give']
    count = request.form['count_give']
    address = request.form['address_give']
    phone = request.form['phone_give']
    doc = {
        'name':name,
        'count':count,
        'address':address,
        'phone':phone,
    }
    db.orders.insert_one(doc)
    return jsonify({'msg': '주문이 완료되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    order = list(db.orders.find({}, {'_id': False}))
    return jsonify({'all_orders': order})

# 작업 예시 html
<script>
        $(document).ready(function () {
            $.ajax({
                type: "GET",
                url: "https://api.manana.kr/exchange/rate.json",
                data: {},
                success: function (response) {
                    let nowRate = response[1]['rate'];
                    $('#rate-box').text(nowRate);
                }
            })
            order_listing();
        });
        function order_listing() {
            $.ajax({
                type: "GET",
                url: "/order",
                data: {},
                success: function (response) {
                    let order = response['all_orders']
                    for (let i=0; i < order.length; i++){
                        let name = order[i]['name']
                        let count = order[i]['count']
                        let address = order[i]['address']
                        let phone = order[i]['phone']
                        let temp_html = `<tr>
                                          <th scope="row">${name}</th>
                                          <td>${count}</td>
                                          <td>${address}</td>
                                          <td>${phone}</td>
                                        </tr>`
                        $("#orders-box").append(temp_html)
                    }
                }
            })
        }
        function order() {
            let name = $("#order-name").val()
            let count = $("#order-count").val()
            let address = $("#order-address").val()
            let phone = $("#order-phone").val()

            $.ajax({
                type: "POST",
                url: "/order",
                data: {name_give:name,'count_give':count, 'address_give':address, 'phone_give':phone},
                success: function (response) { // 성공하면
                    alert(response["msg"]);
                    window.location.reload();
                }
            })
        }
    </script>
