class Battery:  
    def __init__(self, battery_size=70):  
        self.battery_size = battery_size  
  
    def describe_battery(self):  
        print(f"This car has a {self.battery_size}kWh battery.")  
  
    def get_range(self):  
        """打印一条消息，指出电瓶的续航里程"""  
        if self.battery_size == 70:  
            range_value = 240  
        elif self.battery_size == 85:  
            range_value = 270  
        else:  
            range_value = "unknown"  
  
        message = f"This car can go approximately {range_value} miles on a full charge."  
        print(message)  
  
    def upgrade_battery(self):  
        """如果电瓶容量不是85，则将其升级到85"""  
        if self.battery_size != 85:  
            self.battery_size = 85  
            print("Battery has been upgraded to 85kWh.")  

class ElectricCar(Car):  
    def __init__(self, make, model, year):  
        super().__init__(make, model, year)  
        self.battery = Battery()  # 默认情况下，使用70kWh的电瓶  
  
    def get_descriptive_name(self):  
        return f"{self.year} {self.make} {self.model}"  
  
# 示例代码  
my_tesla = ElectricCar('tesla', 'model s', 2016)  
print(my_tesla.get_descriptive_name())  
my_tesla.battery.describe_battery()  
my_tesla.battery.get_range()  
  
# 升级电瓶  
my_tesla.battery.upgrade_battery()  
  
# 再次获取续航里程  
my_tesla.battery.get_range()
