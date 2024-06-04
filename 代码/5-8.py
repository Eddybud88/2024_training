usernames = ['Eric', 'Alice', 'Bob', 'admin', 'Charlie']  
   
for username in usernames:    
    if username == 'admin':  
        print("Hello admin, would you like to see a status report?")  
    else:  
        print("Hello " + username +", thank you for logging in again.")

输出：
Hello Eric, thank you for logging in again.
Hello Alice, thank you for logging in again.
Hello Bob, thank you for logging in again.
Hello admin, would you like to see a status report?
Hello Charlie, thank you for logging in again.
