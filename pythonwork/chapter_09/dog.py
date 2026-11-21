class Dog:
    """一次模拟小狗的游戏"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令是打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)

# 1.访问属性
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} year old.")

# 2.调用方法
my_dog.sit()
my_dog.roll_over()

# 3.创建多个实例
print('\n')
my_dog = Dog('Willie', 9)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} year old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()