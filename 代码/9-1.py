class Restaurant:  
    def __init__(self, restaurant_name, cuisine_type):  
        self.restaurant_name = restaurant_name  
        self.cuisine_type = cuisine_type  
  
    def describe_restaurant(self):  
        print(f"The name of the restaurant is {self.restaurant_name} and it serves {self.cuisine_type}.")  
  
    def open_restaurant(self):  
        print(f"{self.restaurant_name} is now open.")  
  
# 创建一个名为restaurant的实例  
restaurant = Restaurant("Pizza Hut", "Italian")  
  
# 打印两个属性  
print("Restaurant name:", restaurant.restaurant_name)  
print("Cuisine type:", restaurant.cuisine_type)  
  
# 调用describe_restaurant()方法  
restaurant.describe_restaurant()  
  
# 调用open_restaurant()方法  
restaurant.open_restaurant()

输出：
Restaurant name: Pizza Hut  
Cuisine type: Italian  
The name of the restaurant is Pizza Hut and it serves Italian.  
Pizza Hut is now open.
