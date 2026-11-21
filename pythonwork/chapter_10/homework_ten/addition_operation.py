while True:
    firsrt_nummber = input("Please enter somne number:")
    if firsrt_nummber == 'q':
        break
    second = input("Please enter soome number:")
    if second == 'q':
        break
    try:
        print(int(firsrt_nummber) + int(second))
    except ValueError:
        print("You can't enter text!")