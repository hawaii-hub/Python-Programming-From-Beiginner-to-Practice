"""只包含一个user"""

class User:
    """用户简介"""

    def __init__(self, first_name, last_name, age, school):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.school = school
        self.login_attemps = 0

    def descibe_user(self):
        """打印摘要"""
        print(f"name:{self.first_name} {self.last_name}"
              f"\nage:{self.age}"
              f"\nschool:{self.school}")

    def greet_user(self):
        """个性化问候"""
        print(f"hello,{self.first_name.title()} {self.last_name.title()}")

    def incream_login_attemps(self):
        """用来将登录次数+1"""
        self.login_attemps += 1
        return self.login_attemps

    def reset_login_attemps(self):
        """将属性的值重置为0"""
        self.login_attemps = 0
        return self.login_attemps