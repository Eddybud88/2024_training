learning_python.txt:
In Python you can write concise and readable code.  
In Python you can perform complex mathematical operations.  
In Python you can handle data structures like lists, tuples, dictionaries, and sets.  
In Python you can create functions to encapsulate reusable code.  
In Python you can use conditional statements to control program flow.  
In Python you can define classes and create objects with attributes and methods.  
In Python you can manipulate files and directories.  
In Python you can work with web frameworks to build web applications.  
In Python you can interface with databases to store and retrieve data.  
In Python you can create scripts to automate tasks.

# learning_python_reader.py  
  
# 第一次打印：读取整个文件  
with open('learning_python.txt', 'r') as file:  
    print(file.read())  
  
# 第二次打印：遍历文件对象  
with open('learning_python.txt', 'r') as file:  
    for line in file:  
        print(line, end='')  # end='' 避免每行末尾的换行符被打印两次  
  
# 第三次打印：将各行存储在一个列表中，再在 with 代码块外打印它们  
lines = []  
with open('learning_python.txt', 'r') as file:  
    lines = file.readlines()  
  
# 在 with 代码块外打印列表中的行  
for line in lines:  
    print(line, end='')
