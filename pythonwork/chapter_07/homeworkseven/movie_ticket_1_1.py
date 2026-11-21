active = True   #标志位变量，控制循环是否继续

while active:
    age = input("Please enter your age (or 'quit' to exit): ")

    if age == "quit":
        active = False  #设为False，循环下次检查时退出
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15

        print(f"Your tichet costs ${price}.")