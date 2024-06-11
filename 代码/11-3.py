编写类：
class Employee:  
    def __init__(self, first_name, last_name, annual_salary):  
        self.first_name = first_name  
        self.last_name = last_name  
        self.annual_salary = annual_salary  
  
    def give_raise(self, amount=5000):  
        self.annual_salary += amount  
        print(f"{self.first_name} {self.last_name} 的年薪增加了 {amount} 美元，新的年薪是 {self.annual_salary} 美元。")

编写测试用例：
import unittest  
  
class TestEmployee(unittest.TestCase):  
    def setUp(self):  
        # 在每个测试方法之前都会调用 setUp 方法  
        self.employee = Employee('John', 'Doe', 50000)  
  
    def test_give_default_raise(self):  
        # 测试默认加薪  
        self.employee.give_raise()  
        self.assertEqual(self.employee.annual_salary, 55000)  
  
    def test_give_custom_raise(self):  
        # 测试自定义加薪  
        original_salary = self.employee.annual_salary  
        self.employee.give_raise(10000)  
        self.assertEqual(self.employee.annual_salary, original_salary + 10000)  
  
if __name__ == '__main__':  
    unittest.main()
