# 打开文件并读取内容  
with open('learning_python.txt', 'r') as file:  
    lines = file.readlines()  # 读取文件的所有行，每行是一个字符串，包括换行符  
  
# 遍历每一行，将 'Python' 替换为 'C'，并打印修改后的行  
for line in lines:  
    # 使用 str.replace() 方法替换 'Python' 为 'C'  
    # strip() 方法用于移除行首行尾的空白字符（包括换行符）  
    modified_line = line.replace('Python', 'C').strip()  
    print(modified_line)
