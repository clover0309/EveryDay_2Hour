# 구현 요구사항 calculate_order_from_file(file_path) 함수 구현
# 1. 매개변수 file_path로 전달 받은 파일을 연다. *
# 2. 파일 데이터를 읽어서 금액과 수량을 계산한다. *
# 3. 음수 수량이면 ValueError를 발생시킨다. *
# 4. 정상적으로 계산이 끝나면 total_price, total_quantity를 반환함. *

def calculate_order_from_file(file_path) :
    with open(file_path, "r", encoding="utf-8") as file :
    
            total_price = 0
            total_quantity = 0
    
            for i in file :
                parts = i.strip().split(",")
    
                if(int(parts[2]) < 0) :
                    raise ValueError("음수가 발견되었습니다.")
    
                total_price += int(parts[1]) * int(parts[2])
                total_quantity += int(parts[2])

            return total_price, total_quantity

try :
    data = calculate_order_from_file("orders.txt")
    print(f"전체 구매 금액: {data[0]}")
    print(f"전체 구매 수량: {data[1]}")

    with open("order_summary.txt", "w", encoding="utf-8") as summary :
        summary.write(f"전체 구매 금액: {data[0]}\n")
        summary.write(f"전체 구매 수량: {data[1]}")

except ValueError as e :
    print(e)

except FileNotFoundError:
    print("파일이 없습니다.")
