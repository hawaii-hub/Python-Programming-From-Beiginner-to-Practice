age = input("Please enter your age (or 'quit' to exit): ")

while age != 'quit':    #条件直接在while里判断
    age = int(age)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15

    print(f"Your tichet costs ${price}.\n")

    age = input("Please enter your age (or 'quit' to exit): ")      #跟新条件变量