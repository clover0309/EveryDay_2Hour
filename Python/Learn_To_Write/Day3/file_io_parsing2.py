try :
    with open("orders.txt", "r", encoding="utf-8") as file :

        total_price = 0
        total_quantity = 0

        for i in file :
            parts = i.strip().split(",")

            if(int(parts[2]) < 0) :
                raise ValueError("음수가 발견되었습니다.")

            total_price += int(parts[1]) * int(parts[2])
            total_quantity += int(parts[2])

        print(f"전체 구매 금액: {total_price}")
        print(f"전체 구매 수량: {total_quantity}")

    with open("order_summary.txt", "w", encoding="utf-8") as summary :
        summary.write(f"전체 구매 금액: {total_price}\n")
        summary.write(f"전체 구매 수량: {total_quantity}")

except ValueError as e :
    print(e)

except FileNotFoundError:
    print("파일이 없습니다.")
