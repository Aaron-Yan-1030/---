while True:    
    card = input("card number:")
    money = float(input("card money:"))
    if money <= 0:
        print("cannot enter, please charge")
        charge = [10,50,100]
        choice = int(input("select money:1,10;2,50;3,100——"))
        #problem here in line 8
        money += charge[choice - 1]
        #if 判断
        print("success! current money:", money)
    else:
        print("please enter! current money:", money)
        #需替换，列表形式
        number = int(input("how many stations:"))
        if number <= 5:
            price = 3
        elif number <= 11:
            price = 4
        elif number <= 17:
            price = 5
        else:
            price = 6
        
        money -= price
        print("please exit , current money:", money)
