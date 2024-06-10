class User:  
    def __init__(self, first_name, last_name):  
        self.first_name = first_name  
        self.last_name = last_name  
        self.login_attempts = 0  
  
    def increment_login_attempts(self):  
        self.login_attempts += 1  
  
    def reset_login_attempts(self):  
        self.login_attempts = 0  
  
    def describe_user(self):  
        print(f"User Information:")  
        print(f"First Name: {self.first_name}")  
        print(f"Last Name: {self.last_name}")  
        print(f"Login Attempts: {self.login_attempts}")  
  
# 创建一个User实例  
user = User("John", "Doe")  
  
# 调用increment_login_attempts()方法多次  
user.increment_login_attempts()  
user.increment_login_attempts()  
user.increment_login_attempts()  
  
# 打印login_attempts的值，确认它被正确地递增  
user.describe_user()  
  
# 调用reset_login_attempts()方法  
user.reset_login_attempts()  
  
# 再次打印login_attempts的值，确认它被重置为0  
user.describe_user()

输出：
User Information:  
First Name: John  
Last Name: Doe  
Login Attempts: 3  
User Information:  
First Name: John  
Last Name: Doe  
Login Attempts: 0
