def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#w位置实参
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 关键字实参
describe_pet(animal_type='chicken', pet_name='kunkun')
describe_pet(pet_name='kunkun', animal_type='chicken')

# 默认值
def describe_pet_1(name,animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {name.title()}.")

describe_pet_1('white')

# 等效的函数调用， 使用def describe_pet_1(name,ainimal_type='dog'):
#一条名为Willie的小狗
describe_pet_1('Willie')
describe_pet_1(name='Willie')

#一只名为Harry的仓鼠
describe_pet_1('harry', 'hamster')
describe_pet_1(name='harry', animal_type='hamster')
describe_pet_1(animal_type='hamster', name='harry')
