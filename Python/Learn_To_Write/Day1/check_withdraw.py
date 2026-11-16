# balance 변수에 10000을 저장한다.
balance = 10000
# withdraw 변수에 15000을 저장한다.
withdraw = 15000
# 출금액이 잔액보다 크면 "잔액 부족"을 출력한다.
if (balance < withdraw) :
    print("잔액 부족")
# 그렇지 않으면 "출금 가능"을 출력한다
else :
    print("출금 가능")