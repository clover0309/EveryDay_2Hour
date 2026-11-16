# 전체 구매 금액을 저장할 total_price 변수를 선언한다. *
# total_price를 적절한 값으로 초기화한다. *
# 반복문에서 계산한 item_total을 total_price에 누적한다. *
# 반복문이 끝난 다음 전체 구매 금액을 한 번 출력한다. *
# 기존의 상품별 금액 출력은 그대로 유지한다. *
products = [
    {"name": "키보드", "price": 50000, "quantity": 2},
    {"name": "마우스", "price": 20000, "quantity": 3},
    {"name": "모니터", "price": 150000, "quantity": 1}
]

total_price = 0

for product in products :
    item_total = product["price"] * product["quantity"]
    print(item_total)
    total_price += item_total

print(f"전체 구매 금액 : {total_price}")