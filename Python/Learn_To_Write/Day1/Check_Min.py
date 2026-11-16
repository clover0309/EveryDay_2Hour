# min_value를 리스트의 첫 번째 값으로 초기화한다. *
# for 반복문으로 리스트를 순회한다. *
# if 조건문으로 현재 값과 min_value를 비교한다. *
# 더 작은 값을 발견하면 min_value를 변경한다. *
# 반복문이 끝나면 최솟값을 출력한다. *
# min() 내장 함수는 사용하지 않는다. *

numbers = [100]
min_value = numbers[0]

for number in numbers :
    if (min_value > number) :
        min_value = number

print(min_value)