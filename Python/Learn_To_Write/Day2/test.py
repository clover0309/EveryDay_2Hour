def check_quantity(quantity):
    if quantity < 0:
        raise ValueError("수량 오류")

    return quantity

check_quantity(-3)

print("검사 완료")