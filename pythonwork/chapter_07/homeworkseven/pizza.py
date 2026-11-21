prompt = "\nPlease enter the pizza topping you'd like to oder:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    pizza = input(prompt)

    if pizza == 'quit':
        break
    else:
        print(f"Would you like to add this {pizza.title()} to your pizza?!")