loves=['mount tai', 'zhangjiajie', 'yangtze river', 'yellow river', 'mount fuji', 'amazon river', 
       'china', 'italy', 'janpan', 'germany', 'france', 'india', 'switzerland', 'tokyo', 'new york',
       'paris', 'london', 'chicago']
print(loves)

print(len(loves))

print(loves[2])
print(f'I want to visit {loves[17].title()} in the summer vacation.')

loves[0]='mount hua'
print(f'I want to visit {loves[0]} instead of mount tai.')
loves.append('rome')
print(f'I also want to visit {loves[-1]} in the future.')
loves.insert(17, 'hawaii')
print(f'I want to visit {loves[17]} in the future.')
print(loves)

del loves[0]
love=loves.pop(0)
print(f'I don\'t want to visit {love.title()}, so I will remove it from the list.')
print(love)
print(loves)

river = 'yellow river'
loves.remove(river)
print(f'I have been to {river.title()} before, so I will remove it from the list.')
print(loves)

print(sorted(loves))
loves.reverse()
print(loves)