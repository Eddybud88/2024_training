class Restaurant:  
    def __init__(self, name, cuisine_type):  
        self.name = name  
        self.cuisine_type = cuisine_type  
        self.number_served = 0  
  
    def describe_restaurant(self):  
        print(f"The name of the restaurant is {self.name} and it serves {self.cuisine_type} cuisine.")  
  
    def open_restaurant(self):  
        print(f"{self.name} is open.")  
  
    def set_number_served(self, num):  
        self.number_served = num  
  
    def get_number_served(self):  
        return self.number_served  
  
# IceCreamStand类，继承自Restaurant类  
class IceCreamStand(Restaurant):  
    def __init__(self, name, flavors):  
        super().__init__(name, 'Ice Cream')  # 调用父类的初始化方法  
        self.flavors = flavors  # 添加flavors属性  
  
    def show_flavors(self):  
        print(f"Available flavors at {self.name}:")  
        for flavor in self.flavors:  
            print(f"- {flavor}")  
  
# 创建一个IceCreamStand实例，并调用相关方法  
ice_cream_shop = IceCreamStand("Sweet Dreams", ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"])  
  
# 输出餐厅信息  
ice_cream_shop.describe_restaurant()  
  
# 显示冰淇淋口味  
ice_cream_shop.show_flavors()  
  
# 假设餐厅已经服务了100位客人  
ice_cream_shop.set_number_served(100)  
print(f"Number of customers served: {ice_cream_shop.get_number_served()}")  
  
# 假设餐厅开门营业  
ice_cream_shop.open_restaurant()
