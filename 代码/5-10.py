current_users = ['Eric', 'Alice', 'Bob', 'admin', 'Charlie']  
  
new_users = ['David', 'admin', 'Emily', 'Bob', 'Frank']  
 
for new_user in new_users:  
    if new_user in current_users:  
        print(f"Username '{new_user}' is already taken. Please enter a different username.")  
    else:  
        print(f"Username '{new_user}' is available.")

  输出：
Username 'David' is available.
Username 'admin' is already taken. Please enter a different username.
Username 'Emily' is available.
Username 'Bob' is already taken. Please enter a different username.
Username 'Frank' is available.
