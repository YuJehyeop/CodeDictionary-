# Flask
# 작업 순서

# 1. app.py파일, static,templates(index.html)폴더 생성

# 2. app.py파일과 index.html 파일이 잘 연결 되어있는지 확인

# 3. app.py의 post 부분 작업시작
#      1) 읽어올 값 갯수 파악 및 설정
        sample1_receive = request.form['sample1_give']
        sample2_receive = request.form['sample2_give']
        sample3_receive = request.form['sample3_give']
#      2) 딕셔너리 만들어서 db에 저장
        doc = {
            'sample1': sample1_receive,
            'sample2': sample2_receive,
            'sample3': sample3_receive
        }
        db.clientName.insert_one(doc)

# 4. index.html의 type:'post' 부분 작업
#      1) $.ajax 위에 읽어올 값 정의해준다
        let sample1 = $("#sample-name").val()
        let sample2 = $("#sample-count").val()
        let sample3 = $("#sample-address").val()
#      2) 위에서 읽어온 값을 app.py의 post에서 저장 할 수 있게 보내준다.
        data: {'sample1_give': sample1, 'sample2_give': sample2, 'sample3_give': sample3}
#      3) 필요에 의해 type:'post' 부분 마지막에 초기화를 추가해 준다.
        window.location.reload();

# 5. app.py의 GET 부분 작업시작
#      1) 저장된 값을 전부 가져와 잠시 원하는 key값에 넣어준다.
        samples = list(db.clientName.find({}, {'_id': False}))
        return jsonify({'all_samples': samples})

# 6. index.html의 type:'GET' 부분 작업
#      1) success:function 안에 앞에서 저장 한 값을 가져와 원하는 위치에 출력해 준다.
        success: function(response){
            let sample = response['all_samples']

            for (let i=0; i < sample.length; i++){
                let name = sample[i]['name']
                let count = sample[i]['count']
                let address = sample[i]['address']
                let temp_html = ` <tr>
                                        <th> ${name} </th>
                                        <td> ${count} </td>
                                        <td> ${address} </td>
                                </tr> `
                $("#samples-box").append(temp_html)
            }
        }
# 7. 직접 입려해 보면서 구동 확인하고 ROBO 3T로 잘 저장되는지 확인한다.
# 끝
