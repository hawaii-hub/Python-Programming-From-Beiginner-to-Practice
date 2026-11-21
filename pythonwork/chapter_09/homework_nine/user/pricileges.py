"""一个包含三个类的模块"""

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


class Privileges:
    """储存并显示管理员权限"""

    def __init__(self, privileges=None):
        #self.privileges = privileges if privileges else ['can add post', 'can delete post', 'can ban post']
        if privileges:
            self.privileges = privileges
        else:
            self.privileges = ['can add post', 'can delete post', 'can ban user']


    def show_privileges(self):
        """显示管理员的权限"""
        for privilege in self.privileges:
            print(f" -{privilege}")

class Admin(User):
    """显示管理员"""

    def __init__(self, first_name, last_name, age, school, ):
        """
        先初始化父类的属性,再初始化属性privileges作为列表储存字符串
        """

        super().__init__(first_name, last_name, age, school)
        self.privileges = Privileges() #用子类继承父类的属性后，新建一个属性作为列表储存字符串


