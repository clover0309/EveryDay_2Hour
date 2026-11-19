def calculate_order_from_file(file_path) :
        with open(file_path, "r", encoding="utf-8") as file :
            total_price = 0
            total_quantity = 0

            for i in file :
                line = i.strip()

                # 빈줄 체크
                if (line == "") :
                    continue

                # 코드의 순서를 생각을 잘해보자.
                parts = line.split(",")

                # 필드 길이 체크
                if (len(parts) != 3) :
                    raise ValueError("필드의 길이가 정확히 3개여야 합니다.")

                price = int(parts[1])
                quantity = int(parts[2])

                # 음수 검증
                if (price < 0 or quantity < 0) :
                    raise ValueError("수량 및 가격이 음수입니다.")

                total_price += price * quantity
                total_quantity += quantity

            return total_price, total_quantity


try :
    data = calculate_order_from_file("orders.txt")

    print(f"전체 구매 금액: {data[0]}")
    print(f"전체 구매 수량: {data[1]}")

    with open ("order_summary.txt", "w", encoding="utf-8") as file :
        file.write(f"전체 구매 금액: {data[0]}\n")
        file.write(f"전체 구매 수량: {data[1]}")

except ValueError as e :
    print(e)

except FileNotFoundError as e :
    print(e)