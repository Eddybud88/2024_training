import json  
  
# 定义文件名  
file_name = 'favorite_number.json'  
  
try:  
    # 尝试从JSON文件中读取数字  
    with open(file_name, 'r') as file:  
        favorite_number = json.load(file)  
      
    # 打印消息和读取的数字  
    print(f"I know your favorite number! It’s {favorite_number}.")  
except FileNotFoundError:  
    # 如果文件不存在，则提示用户输入  
    favorite_number = input("请输入你喜欢的数字: ")  
      
    # 尝试将输入转换为整数，如果失败则提示用户重新输入  
    try:  
        favorite_number = int(favorite_number)  
    except ValueError:  
        print("输入无效，请输入一个整数。")  
        exit()  
      
    # 将数字写入JSON文件  
    with open(file_name, 'w') as file:  
        json.dump(favorite_number, file)  
      
    print(f"你喜欢的数字 {favorite_number} 已经被保存到 {file_name} 文件中。")  
except json.JSONDecodeError:  
    # 如果文件存在但内容无效，则提示用户输入并覆盖文件  
    print(f"文件 {file_name} 格式不正确，请重新输入你喜欢的数字。")  
    favorite_number = input("请输入你喜欢的数字: ")  
      
    # 尝试将输入转换为整数，如果失败则提示用户重新输入  
    try:  
        favorite_number = int(favorite_number)  
    except ValueError:  
        print("输入无效，请输入一个整数。")  
        exit()  
      
    # 覆盖无效的文件，将数字写入JSON文件  
    with open(file_name, 'w') as file:  
        json.dump(favorite_number, file)  
      
    print(f"你喜欢的数字 {favorite_number} 已经被保存到 {file_name} 文件中。")  
  
# 运行程序两次以测试功能  
# 第一次运行：应该提示输入数字并保存  
# 第二次运行：应该读取并显示数字
