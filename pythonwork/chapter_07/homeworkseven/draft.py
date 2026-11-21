sandwich_orders = ['tuna', 'chicken', 'beef', 'vegetable', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("The delicatessen has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich.title()}.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwichs have been made: ")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")