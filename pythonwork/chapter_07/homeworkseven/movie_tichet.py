while True:

    age  = input("Please enter your age: ")
    if age == 'quit':
        break
    
    age = int(age)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15

    print(f"Your tichet costs ${price}.")