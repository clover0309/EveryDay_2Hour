# 초기 변수
balance = 10000
withdraw = 15000

# 출금액이 0 이하라면 "잘못된 출금액" 출력
if (withdraw <= 0):
    print("잘못된 출금액")

# 출금액이 잔액보다 크다면 "잔액 부족" 출력
elif (withdraw > balance):
    print("잔액 부족")

# 위 조건에 해당하지 않으면 "출금 가능" 출력
else :
    print("출금 가능")

# 아직 실제 잔액을 차감하지는 않기