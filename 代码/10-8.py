cats.txt：
Luna  
Bella  
Oliver
dogs.txt：
Max  
Buddy  
Molly

def read_and_print_file(filename):  
    try:  
        with open(filename, 'r', encoding='utf-8') as file:  
            contents = file.read()  
            print(f"Contents of {filename}:\n{contents}\n")  
    except FileNotFoundError:  
        print(f"Error: The file {filename} does not exist.")  
  
# 尝试读取并打印 cats.txt 和 dogs.txt 的内容  
filenames = ['cats.txt', 'dogs.txt']  
for filename in filenames:  
    read_and_print_file(filename)

输出：
Contents of cats.txt:  
Luna  
Bella  
Oliver  
  
Error: The file dogs.txt does not exist.
