import json  
  
def get_stored_username():  
    """如果存储了用户名，就获取它，并询问用户是否正确"""  
    filename = 'username.json'  
    try:  
        with open(filename, 'r') as f_obj:  
            username = json.load(f_obj)  
            # 询问用户用户名是否正确  
            while True:  
                if input(f"Is '{username}' your name? (yes/no) ").lower() == 'yes':  
                    return username  
                else:  
                    return None  
    except FileNotFoundError:  
        return None  
  
def get_new_username():  
    """提示用户输入用户名并保存到文件"""  
    username = input("What is your name? ")  
    filename = 'username.json'  
    with open(filename, 'w') as f_obj:  
        json.dump(username, f_obj)  
    return username  
  
def greet_user():  
    """问候用户，并指出其名字"""  
    username = get_stored_username()  
    if username:  
        print("Welcome back, " + username + "!")  
    else:  
        username = get_new_username()  
        print("We'll remember you when you come back, " + username + "!")  
  
greet_user()
