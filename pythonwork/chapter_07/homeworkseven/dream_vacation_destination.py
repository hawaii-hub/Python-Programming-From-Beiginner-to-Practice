responses = {}
active = True

while active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world,where would you go?")

    responses[name] = response

    repeat = input("Would you like to let anther person respond? (yes/no)")
    if repeat == 'no':
        active = False

print("\n--- Poll Results ---")
for name,response in responses.items():
    print(f"{name} would like to visit {response}.")