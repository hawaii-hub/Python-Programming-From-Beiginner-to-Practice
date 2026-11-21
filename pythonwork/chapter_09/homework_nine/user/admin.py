"""一个包含另一个"""

from  user import User
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
    """显示管理员的权限"""

    def __init__(self, first_name, last_name, age, school, *privileges):
        """
        先初始化父类的属性,再初始化属性privileges作为列表储存字符串
        """

        super().__init__(first_name, last_name, age, school)
        self.privileges = privileges #用子类继承父类的属性后，新建一个属性作为列表储存字符串

    def show_privileges(self):
            """显示管理员的权限"""
            for privilege in self.privileges:
                print(f" -{privilege}")

