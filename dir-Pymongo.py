# 파이몽고 기본코드
    from pymongo import MongoClient
    client = MongoClient('localhost', 27017)          # 내 컴퓨터에서 돌아가고있는 mongoDB에 접속 할 겁니다.
    db = client.dbsparta                              # dbsparta 라는 db 이름으로 접속 할 겁니다.


  # 1) insert  -> 딕셔너리 만들어서 몽고에 넣는다.(mongoDB는 딕셔너리가 쌓이는 것이다.)
    doc = {'name':'bobby','age':21}
    db.users.insert_one(doc)     # 위 doc(딕셔너리)를 users에 넣어준다.(db > users > insert_one(doc))

  # 2) find
    user = db.users.find_one({'name':'bobby'},{})                # 한개만 찾기
    same_ages = list(db.users.find({'age':21},{'_id':False}))    #  age:21 인값 표시 하지만 _id는 표시하지 않는다.
    same_ages = list(db.users.find({},{'_id':False}))            # find{}값을 비워둔경우 모든 값을 가져온다.

  # 3) update
    db.users.update_one({'name':'bobby'},{'$set':{'age':19}})    # name이 bobby인 것을 찾아 age를 19로 바꿔라.
    db.users.update_many({'name':'bobby'},{'$set':{'age':19}})   # name이 bobby인 것을 모두 찾아 age를 19로 바꿔라.(위험해서 잘 쓰지 않는다.)

  # 4) delete
    db.users.delete_one({'name':'bobby'})      # 해당 값 하나 지우기
    db.users.delete_many({'name':'bobby'})     # 해당 값 다 지우기 (위험 잘안쓰임)