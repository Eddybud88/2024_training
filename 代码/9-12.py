user_module.py：
class User:  
    def __init__(self, first_name, last_name, username):  
        self.first_name = first_name  
        self.last_name = last_name  
        self.username = username  
  
    def describe_user(self):  
        print(f"\nUser {self.username} is {self.first_name} {self.last_name}.")

admin_module.py：
from user_module import User  
  
class Privileges:  
    def __init__(self, privileges=[]):  
        self.privileges = privileges  
  
    def show_privileges(self):  
        print("Privileges:")  
        for privilege in self.privileges:  
            print("- " + privilege)  
  
class Admin(User):  
    def __init__(self, first_name, last_name, username):  
        super().__init__(first_name, last_name, username)  
        self.privileges = Privileges(['can add user', 'can delete user', 'can ban user'])  
  
    def show_privileges(self):  
        print("\nAdmin privileges:")  
        self.privileges.show_privileges()

main:
from admin_module import Admin  
  
# Create an Admin instance  
admin = Admin('John', 'Doe', 'johndoe')  
  
# Call the show_privileges method  
admin.show_privileges()

输出：
Admin privileges:  
Privileges:  
- can add user  
- can delete user  
- can ban user
