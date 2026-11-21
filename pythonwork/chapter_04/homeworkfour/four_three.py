#4.3 数到20
for value in range(1,21):
    print(value)

#4.4 100万
numbers = list(range(1,1_000_000))
#for number in numbers:
    #print(number)

#4.5 100万求和
print('')
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4.6 奇数
print('')
odd_numbers = list(range(1,21,2))
print(odd_numbers)
for odd_number in odd_numbers:
    print(odd_number)

#4.7 3的倍数
print('')
multiples_of_three = list(range(3,31,3))
for multiple_of_three in multiples_of_three:
    print(multiple_of_three)

#4.8 立方
print('')
cubes = []
for one in range(1,11):
    cubes.append(one**3)

for te in cubes:
    print(te)

#4.9 立方推导式
print('')
squares = [s**3 for s in range(1,11)]
print(squares)