class Privileges:  
    def __init__(self):  
        self.privileges = ["can add post", "can delete post", "can ban user"]  
  
    def show_privileges(self):  
        print("\nPrivileges:")  
        for privilege in self.privileges:  
            print(f"- {privilege}")  
  
# 继承User类的Admin类  
class Admin(User):  
    def __init__(self, first_name, last_name):  
        super().__init__(first_name, last_name)  # 调用父类的初始化方法  
        self.privileges = Privileges()  # 创建一个Privileges实例并赋值给admin的privileges属性  
  
    # 现在Admin类不再需要show_privileges方法，因为Privileges类已经包含了它  
  
# 创建一个Admin实例，并使用Privileges的show_privileges方法来显示其权限  
admin_user = Admin("John", "Doe")  
# 注意：我们现在通过admin_user.privileges来访问Privileges类的实例  
admin_user.privileges.show_privileges()

输出：
Privileges:  
- can add post  
- can delete post  
- can ban user
