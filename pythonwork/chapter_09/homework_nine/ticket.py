from random import choice

couples = ['a', 's', 'd', 'f', 'g', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#中奖号码
winning_ticket = []
for i in range(4):
    ticket = choice(couples)
    winning_ticket.append(ticket)

print(f"中奖号码: {winning_ticket}")

#我的号码
my_ticket = ['a', 4, 5, 8]

#判断
if my_ticket == winning_ticket:
    print("恭喜您,中大奖了")
else:
    print("很遗憾,没中奖")