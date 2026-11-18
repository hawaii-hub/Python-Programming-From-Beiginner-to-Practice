class Employee:
    """收集雇员信息"""

    def __init__(self, first_name, second_name, annual_salary):
        """储存姓,名,年薪"""
        self.first_name = first_name
        self.second_name = second_name
        self.annual_salary = annual_salary
        
    def give_raise(self,addition=5000):
        """默认将年薪增加五千美元"""
        self.annual_salary += addition