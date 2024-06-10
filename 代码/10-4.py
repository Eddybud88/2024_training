def write_to_guest_book(name):  
    with open('guest_book.txt', 'a', encoding='utf-8') as file:  
        file.write(name + '\n')  
  
while True:  
    name = input("请输入您的名字（输入'exit'退出）: ")  
    if name.lower() == 'exit':  
        break  
      
    print(f"您好，{name}！欢迎访问。")  
    write_to_guest_book(name)  
  
print("再见，祝您愉快！")
