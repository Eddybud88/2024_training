restaurant_module.py：
class Restaurant:  
    def __init__(self, restaurant_name, cuisine_type):  
        self.restaurant_name = restaurant_name  
        self.cuisine_type = cuisine_type  
        self.number_served = 0  
  
    def describe_restaurant(self):  
        return f"{self.restaurant_name} serves {self.cuisine_type}."  
  
    def open_restaurant(self):  
        return f"{self.restaurant_name} is open."  
  
    def set_number_served(self, num_customers):  
        if num_customers >= 0:  
            self.number_served = num_customers  
        else:  
            print("Number served cannot be negative.")  
  
    def increment_number_served(self, additional_customers):  
        self.number_served += additional_customers

  导入：
from restaurant_module import Restaurant  
  
# 创建一个 Restaurant 实例  
my_restaurant = Restaurant("Tasty Burgers", "Burgers")  
  
# 调用 describe_restaurant 方法  
print(my_restaurant.describe_restaurant())  
  
# 调用 open_restaurant 方法  
print(my_restaurant.open_restaurant())  
  
# 调用 set_number_served 方法  
my_restaurant.set_number_served(50)  
print(f"Number of customers served: {my_restaurant.number_served}")  
  
# 调用 increment_number_served 方法  
my_restaurant.increment_number_served(10)  
print(f"Number of customers served after additional 10: {my_restaurant.number_served}")

输出：
Tasty Burgers serves Burgers.  
Tasty Burgers is open.  
Number of customers served: 50  
Number of customers served after additional 10: 60
