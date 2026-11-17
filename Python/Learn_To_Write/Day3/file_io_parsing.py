# 파일을 열때, FileNotFoundError가 발생할 수 있으니, with문 전에 try를 통해 예외처리를 대비하자.
try :
    with open("orders.txt", "r", encoding="utf-8") as file :
        # 초기 작성 
        # if (file.closed == True) :
        # raise FileNotFoundError("파일이 없습니다.")
        total_price = 0
        total_quantity = 0
        
        for i in file :
            parts = i.strip().split(",")
            
            # 초기 작성 : if (parts[2] < 0) :
            if (int(parts[2]) < 0) :
                raise ValueError("수량이 음수입니다.")

            total_price += int(parts[1]) * int(parts[2])
            total_quantity += int(parts[2])

        print(f"전체 구매 금액: {total_price}")
        print(f"전체 구매 수량: {total_quantity}")

except ValueError as e :
    print(e)

except FileNotFoundError as e :
    print(e)
