# max_value 변수를 선언하고 초기화한다. *
# for 반복문을 이용해 리스트를 순회한다. *
# if 조건문으로 현재 숫자와 max_value를 비교한다. *
# 더 큰 숫자를 발견하면 max_value를 변경한다. *
# 반복문 종료 후 최댓값을 출력한다. *
# max() 내장 함수는 사용하지 않는다. *

numbers = [15, 42, 8, 67, 23]
max_value = numbers[0]

for number in numbers :
    max_value = number
    if max_value < number :
        max_value = number

print(max_value)
