# 위 products 데이터를 선언한다. *
# for 반복문으로 리스트를 순회한다. *
# 각 딕셔너리에서 "name" 키에 해당하는 값만 꺼낸다. *
# print()로 상품명을 하나씩 출력한다. *
# 아직 가격이나 수량은 계산하지 않는다. *
products = [
    {"name": "키보드", "price": 50000, "quantity": 2},
    {"name": "마우스", "price": 20000, "quantity": 3},
    {"name": "모니터", "price": 150000, "quantity": 1}
]

for product in products :
    print(product["name"])