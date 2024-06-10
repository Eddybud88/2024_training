class User:  
    def __init__(self, first_name, last_name):  
        self.first_name = first_name  
        self.last_name = last_name  
  
    def describe_user(self):  
        print(f"User: {self.first_name} {self.last_name}")  
  
# 继承User类的Admin类  
class Admin(User):  
    def __init__(self, first_name, last_name):  
        super().__init__(first_name, last_name)  # 调用父类的初始化方法  
        self.privileges = ["can add post", "can delete post", "can ban user"]  # 添加权限属性  
  
    def show_privileges(self):  
        print("\nAdmin privileges:")  
        for privilege in self.privileges:  
            print(f"- {privilege}")  
  
# 创建一个Admin实例，并调用show_privileges方法  
admin_user = Admin("John", "Doe")  
admin_user.describe_user()  
admin_user.show_privileges()
