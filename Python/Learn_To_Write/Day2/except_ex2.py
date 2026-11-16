products = [
    {"name": "키보드", "price": 0, "quantity": 0},
    {"name": "마우스", "price": 0, "quantity": 0}
]


def calculate_order(products):
    total_price = 0
    total_quantity = 0

    for product in products :
        if(product["quantity"] < 0) :
            raise ValueError("수량은 음수일 수 없습니다.")

        total_price += product["price"] * product["quantity"]
        total_quantity += product["quantity"]

    return total_price, total_quantity


try :
    result = calculate_order(products)
    print(f"전체 구매 금액: {result[0]}")
    print(f"전체 구매 수량: {result[1]}")

except ValueError as e :
    print(e)

# 예외가 발생 할 수도 있으니, try문 내부로 옮겨야함.
# print(f"전체 구매 금액: {result[0]}")
# print(f"전체 구매 수량: {result[1]}")
