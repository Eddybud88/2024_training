import os  
  
# 检查文件是否存在  
if os.path.exists('guest.txt'):  
    print("文件guest.txt已存在，将追加内容。")  
  
# 提示用户输入名字  
name = input("请输入您的名字: ")  
  
# 打开文件，准备写入内容  
# 如果文件不存在，'a'模式会创建文件；如果文件已存在，'a'模式会追加内容到文件末尾  
with open('guest.txt', 'a', encoding='utf-8') as file:  
    # 写入名字和换行符（以便下次写入时在新的一行）  
    file.write(name + '\n')  
  
# 提示用户写入成功  
print("您的名字已成功写入到guest.txt文件中。")
