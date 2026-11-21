# 6.1man
people_1 = {
    'first_name': 'jingrui',
    'last_name': 'liu',
    'age': 'yunchengyizhong',
    'city': 'yuncheng'
}

people_2 = {
    'first_name': 'shan',
    'last_name': 'li',
    'age': '郓城一中',
    'city': '郓城'
}

people = [people_1, people_2]
for people_0 in people:
    print(people_0)  # 6.7 人们

# 6.2喜欢的数
print('\nFavorite number')

favorite_numbers = {
    'bod': '2',
    'alice': '6',
    'eve': '7',
    'diana': '9',
    'frank': '3'
}

print(favorite_numbers)

# 词汇表集合
print('\nDictionary:')

dictionary = {
    'dictionary': '键值对集合',
    '变量': '可以储存值的盒子',
    '字符串': '一系列字符',
    '列表': '一系列元素的组成',
    'if': '执行条件测试',
}

#print(dictionary['dictionary'])
#print(dictionary['变量'])

# homework6.4 词汇表2
#for key, value in dictionary.items():
    #print(f"{key}:{value}")

# 添加5个python术语
dictionary['function'] = '可重复使用的代码块,用def定义'
dictionary['循环loop'] = '重复执行代码块--for遍历序列,while条件循环'
dictionary['方法method'] = '属于某个对象的函数'
dictionary['索引'] = '序列元素的位置编号,从0开始'
dictionary['布尔值'] = '只有真和假两种值'

for key, value in dictionary.items():
    print(f"{key}:{value}")