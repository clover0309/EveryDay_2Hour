# for 반복문으로 상품을 하나씩 가져온다. *
# 각 상품의 price와 quantity를 곱한다. *
# 계산한 상품별 금액을 print()로 출력한다. *
# 아직 전체 합계는 구하지 않는다. *
products = [
    {"name": "키보드", "price": 50000, "quantity": 2},
    {"name": "마우스", "price": 20000, "quantity": 3},
    {"name": "모니터", "price": 150000, "quantity": 1}
]

item_total = 0

for product in products :
    item_total = product["price"] * product["quantity"]
    print(item_total)