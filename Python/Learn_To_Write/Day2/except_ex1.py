# 음수로 고의 ValueError에 해당되게 지정
quantity = 5

try :
    if (quantity < 0) :
        # 음수 임으로 여기서 걸림.
        raise ValueError("수량은 음수 일 수 없습니다.")
    # 정상인 경우 "정상 수량" 출력
    print("정상 수량")

# raise에서 걸린게, except으로 넘어감
except ValueError as e :
    print(e)

# 검사가 다 끝났으니, except문 밖에서 "검사 완료" 출력
print("검사 완료")