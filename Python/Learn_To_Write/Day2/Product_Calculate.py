products = [
    {"name": "키보드", "price": 0, "quantity": 3},
    # {"name": "마우스", "price": 20000, "quantity": 3},
    # {"name": "모니터", "price": 150000, "quantity": 1}
]

def calculate_order(products) :
    # total_price, total_quantity = 0
    total_price = 0
    total_quantity = 0

    for product in products :
        total_price += product["price"] * product["quantity"]
        total_quantity += product["quantity"]

    return total_price, total_quantity

result = calculate_order(products)

print(f"전체 구매 금액: {result[0]}")
print(f"전체 구매 수량: {result[1]}")