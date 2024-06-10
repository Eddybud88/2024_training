class Restaurant:  
    def __init__(self, restaurant_name, cuisine_type):  
        self.restaurant_name = restaurant_name  
        self.cuisine_type = cuisine_type  
        self.number_served = 0  
  
    def describe_restaurant(self):  
        print(f"The name of the restaurant is {self.restaurant_name} and it serves {self.cuisine_type}.")  
  
    def open_restaurant(self):  
        print(f"{self.restaurant_name} is now open.")  
  
    def set_number_served(self, number):  
        self.number_served = number  
  
    def increment_number_served(self, increment_by):  
        self.number_served += increment_by  
  
# 创建一个名为restaurant的实例  
restaurant = Restaurant("Pizza Hut", "Italian")  
  
# 打印有多少人在这家餐馆就餐过  
print(f"Number of people served: {restaurant.number_served}")  
  
# 修改就餐人数  
restaurant.set_number_served(100)  
print(f"Number of people served after setting: {restaurant.number_served}")  
  
# 调用increment_number_served方法，并假设每天可能接待200人  
restaurant.increment_number_served(200)  
print(f"Number of people served after increment: {restaurant.number_served}")

输出：
Number of people served: 0  
Number of people served after setting: 100  
Number of people served after increment: 300
