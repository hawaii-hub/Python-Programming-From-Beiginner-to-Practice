sandwich_orders = ['tuna', 'chicken', 'beef', 'vegetablea']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich.title()}.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwichs have been made: ")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")