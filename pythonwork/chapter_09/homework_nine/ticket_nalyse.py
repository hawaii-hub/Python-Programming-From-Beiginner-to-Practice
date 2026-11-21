from random import choice

couples = ['a', 's', 'd', 'f', 'g', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

my_ticket = ['a', 4, 5, 8]  #选的号码
attmpts = 0  #抽奖次数 

#中奖号码
while True:
    winning_ticket = []
    for i in range(4):
        ticket = choice(couples)
        winning_ticket.append(ticket)

    attmpts += 1

    if winning_ticket == my_ticket:
        break

#结论
print(f"抽了 {attmpts}次 才中将")
print(f"中奖号码: {winning_ticket}")