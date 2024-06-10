user_module.py：
# user_module.py  
  
class Privileges:  
    def __init__(self, privileges=[]):  
        self.privileges = privileges  
  
    def show_privileges(self):  
        print("Privileges:")  
        for privilege in self.privileges:  
            print("- " + privilege)  
  
  
class User:  
    def __init__(self, first_name, last_name, username):  
        self.first_name = first_name  
        self.last_name = last_name  
        self.username = username  
        self.privileges = Privileges()  
  
    def describe_user(self):  
        print(f"\nUser {self.username} is {self.first_name} {self.last_name}.")  
  
    def add_privilege(self, privilege):  
        self.privileges.privileges.append(privilege)  
  
  
class Admin(User):  
    def __init__(self, first_name, last_name, username):  
        super().__init__(first_name, last_name, username)  
        self.privileges.privileges = ['can add user', 'can delete user', 'can ban user']  
  
    def show_privileges(self):  
        print("\nAdmin privileges:")  
        super().show_privileges()  # Call the inherited show_privileges method  
        # Add additional privileges for Admin  
        for privilege in self.privileges.privileges:  
            print("- " + privilege)  
  
# This part is optional, just to demonstrate how to use the classes within the module  
# admin = Admin('John', 'Doe', 'johndoe')  
# admin.show_privileges()

# main.py  
  
from user_module import Admin  
  
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
- can add user  
- can delete user  
- can ban user
