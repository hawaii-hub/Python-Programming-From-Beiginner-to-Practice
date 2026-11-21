from random import randint

class Die:
    """n面骰子"""

    def __init__(self, sides=6):
        """骰子默认6面"""
        self.sides = sides

    def roll_die(self):
        """随机打印1-sides的数"""
        return randint(1, self.sides)

# 6面骰子，扔出10次
die_6 = Die()
print("6面骰子扔10次")
for i in range(10):
    print(die_6.roll_die(),end=" ")
print()

#十面骰子，扔 10次
die_10 = Die(10)
print("\n十面骰子扔10次:")
for i in range(10):
    print(die_10.roll_die(),end=" ")
print()

# 二十面骰子，扔 20次
die_20 = Die(20)
print("\n二十面骰子扔10次")
for i in range(10):
    print(die_20.roll_die(),end=" ")
print()