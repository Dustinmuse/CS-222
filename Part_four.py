def stocks():

    target_price = float(input("Enter what price you want to sell your stocks at: "))

    while True:
        current_stock_price = 5.26
        if target_price <= current_stock_price:
            print("Shares can be sold now.")
            break
        else:
            current_stock_price += 3.12