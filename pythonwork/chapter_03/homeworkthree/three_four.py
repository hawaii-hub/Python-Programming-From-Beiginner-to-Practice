#3.4
dinner_guests=['bill gates','steve jobs','elon musk']
print(f'I would like to invite {dinner_guests[0].title()} to dinner.')
print(f'I would like to invite {dinner_guests[1].title()} to dinner.')
print(f'I would like to invite {dinner_guests[2].title()} to dinner.')

#3.5
print('')

print(f'{dinner_guests[0].title()} can not come to dinner.')
dinner_guests[0]='mark zuckerberg'
print(f'I would like to invite {dinner_guests[0].title()} to dinner.')
print(f'I would like to invite {dinner_guests[1].title()} to dinner.')
print(f'I would like to invite {dinner_guests[2].title()} to dinner.')

#3.6
print('')

print('I found a bigger dinner table!')
dinner_guests.insert(0,'ernest hemingway')
print(f'I would like to invite {dinner_guests[0].title()} to dinner.')
dinner_guests.insert(3,'j.k. rowling')
print(f'I would like to invite {dinner_guests[2].title()} to dinner.')
dinner_guests.append('lsaac asimov')
print(f'I would like to invite {dinner_guests[5].title()} to dinner.')

#3.7
print('')

print(dinner_guests)
print(len(dinner_guests))
print('I can only invite two people to dinner.')
removed_guest=dinner_guests.pop(0)
print(f"I'm sorry {removed_guest.title()},I can't invite you to dinner.")
removed_guest=dinner_guests.pop(0)
print(f"I'm sorry {removed_guest.title()},I can't invite you to dinner.")
removed_guest=dinner_guests.pop(0)
print(f"I'm sorry {removed_guest.title()},I can't invite you to dinner.")
removed_guest=dinner_guests.pop(1)
print(f"I'm sorry {removed_guest.title()},I can't invite you to dinner.")

#剩下两位小说作者
print(len(dinner_guests))
print(f'{dinner_guests[0].title()} and {dinner_guests[1].title()} are still invited to dinner.')

#删除剩下两位
del dinner_guests[1]
del dinner_guests[0]
print(dinner_guests)



