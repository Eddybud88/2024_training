class Restaurant:  
    def __init__(self, restaurant_name, cuisine_type):  
        self.restaurant_name = restaurant_name  
        self.cuisine_type = cuisine_type  
  
    def describe_restaurant(self):  
        print(f"The name of the restaurant is {self.restaurant_name} and it serves {self.cuisine_type}.")  
  
    def open_restaurant(self):  
        print(f"{self.restaurant_name} is now open.")  
  
# 创建第一个实例：Pizza Hut  
restaurant1 = Restaurant("Pizza Hut", "Italian")  
restaurant1.describe_restaurant()  
  
# 创建第二个实例：Thai House  
restaurant2 = Restaurant("Thai House", "Thai")  
restaurant2.describe_restaurant()  
  
# 创建第三个实例：Sushi Bar  
restaurant3 = Restaurant("Sushi Bar", "Japanese")  
restaurant3.describe_restaurant()


输出：
The name of the restaurant is Pizza Hut and it serves Italian.  
The name of the restaurant is Thai House and it serves Thai.  
The name of the restaurant is Sushi Bar and it serves Japanese.
