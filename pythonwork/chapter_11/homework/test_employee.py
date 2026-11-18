import pytest
from employee import Employee

@pytest.fixture
def employee():
    """一个可以供所有人使用的实例"""
    employee = Employee('john', 'doe', 50000)
    return employee

def test_give_default_raise(employee):
    """测试默认增加的年薪"""
    employee.give_raise()
    assert  employee.annual_salary == 55000

def test_give_custom_raise(employee):
    """测试自定义增加的年薪"""
    employee.give_raise(50000)
    assert  employee.annual_salary == 100000
    