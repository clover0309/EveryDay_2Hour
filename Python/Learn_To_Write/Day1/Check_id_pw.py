# user_id = "admin"과 password = "1234"를 선언한다.
user_id = "guest"
password = "0000"

# 아이디와 비밀번호가 모두 일치하면 "로그인 성공"을 출력한다.
if user_id == "admin" and password == "1234" :
    print("로그인 성공")

# 하나라도 일치하지 않으면 "로그인 실패"를 출력한다.
else :
    print("로그인 실패")
