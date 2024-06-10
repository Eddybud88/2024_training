import json  
  
# 提示用户输入他喜欢的数字  
favorite_number = input("请输入你喜欢的数字: ")  
  
# 尝试将输入转换为整数，如果失败则提示用户重新输入  
try:  
    favorite_number = int(favorite_number)  
except ValueError:  
    print("输入无效，请输入一个整数。")  
    exit()  
  
# 定义文件名  
file_name = 'favorite_number.json'  
  
# 将数字写入JSON文件  
with open(file_name, 'w') as file:  
    json.dump(favorite_number, file)  
  
print(f"你喜欢的数字 {favorite_number} 已经被保存到 {file_name} 文件中。")

import json  
  
# 定义文件名  
file_name = 'favorite_number.json'  
  
try:  
    # 从JSON文件中读取数字  
    with open(file_name, 'r') as file:  
        favorite_number = json.load(file)  
      
    # 打印消息  
    print(f"I know your favorite number! It’s {favorite_number}.")  
except FileNotFoundError:  
    print(f"文件 {file_name} 不存在，无法读取你喜欢的数字。")  
except json.JSONDecodeError:  
    print(f"文件 {file_name} 格式不正确，无法解码数字。")
