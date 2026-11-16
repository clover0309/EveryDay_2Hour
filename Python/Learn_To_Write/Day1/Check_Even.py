# count 변수를 0으로 초기화한다. *
# for 반복문으로 리스트를 순회한다. *
# 현재 숫자가 짝수인지 if 조건문으로 판단한다. *
# 짝수라면 count를 1 증가시킨다. *
# 반복문 종료 후 개수를 출력한다. *
numbers = [3, 8, 12, 7, 15, 20, 4]
count = 0

for number in numbers :
    if(number % 2 == 0) :
        count += 1

print(count)