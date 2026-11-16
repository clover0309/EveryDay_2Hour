# 초기 변수
numbers = [10, 20, 30, 40, 50]

# total 변수를 0으로 초기화한다.
total = 0
# for 반복문으로 리스트의 숫자를 하나씩 가져온다.
for number in numbers :
# += 연산자를 이용해 total에 숫자를 누적한다.
    total += number
# 반복문이 끝나면 total을 한 번만 출력한다.
print(total)
# sum() 내장 함수는 사용하지 않는다.