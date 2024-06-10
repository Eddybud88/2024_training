class User:  
    def __init__(self, first_name, last_name, age=None, email=None):  
        self.first_name = first_name  
        self.last_name = last_name  
        self.age = age  
        self.email = email  
  
    def describe_user(self):  
        print(f"User Information:")  
        print(f"First Name: {self.first_name}")  
        print(f"Last Name: {self.last_name}")  
        if self.age:  
            print(f"Age: {self.age}")  
        if self.email:  
            print(f"Email: {self.email}")  
  
    def greet_user(self):  
        print(f"Hello, {self.first_name} {self.last_name}! Nice to meet you.")  
  
# 创建多个表示不同用户的实例  
user1 = User("Alice", "Smith", 30, "alice@example.com")  
user2 = User("Bob", "Johnson", 25)  
user3 = User("Charlie", "Brown", email="charlie@example.com")  
  
# 对每个实例都调用上述两个方法  
user1.describe_user()  
user1.greet_user()  
print()  # 打印一个空行以分隔输出  
  
user2.describe_user()  
user2.greet_user()  
print()  # 打印一个空行以分隔输出  
  
user3.describe_user()  
user3.greet_user()
