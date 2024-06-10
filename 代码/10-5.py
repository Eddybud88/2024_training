# 初始化一个空字符串，用于检测用户是否想要退出循环  
exit_phrase = 'exit'  
  
# 尝试打开文件以追加模式，如果文件不存在则创建它  
with open('reasons_for_coding.txt', 'a', encoding='utf-8') as file:  
    # 使用一个空字符串来写入文件头（如果需要的话）  
    # 例如: file.write("Reasons for coding:\n")  
      
    while True:  
        # 询问用户为何喜欢编程  
        reason = input("请输入您喜欢编程的原因（输入'exit'退出）: ")  
          
        # 检查用户是否想要退出循环  
        if reason.lower() == exit_phrase:  
            print("感谢您的输入，再见！")  
            break  
          
        # 将用户输入的原因写入文件  
        file.write(reason + '\n')  
          
        # 可以在这里添加额外的逻辑，比如打印用户输入的原因到屏幕上  
        print(f"您喜欢编程的原因是：{reason}")  
  
# 循环结束后，文件已关闭，无需进行额外的关闭操作
