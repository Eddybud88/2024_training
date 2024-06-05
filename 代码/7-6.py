while True:  # 直接使用无限循环  
    # 询问用户年龄  
    age_input = input("请输入您的年龄（或输入'quit'退出）：")  
      
    # 检查用户是否想退出  
    if age_input.lower() == 'quit':  
        break  # 使用 break 语句退出循环  
    else:  
        try:  
            age = int(age_input)  
              
            # 根据年龄计算票价  
            if age < 3:  
                price = "免费"  
            elif 3 <= age <= 12:  
                price = "10 美元"  
            else:  
                price = "15 美元"  
              
            # 告诉用户他们的票价  
            print(f"您的票价是：{price}")  
        except ValueError:  
            print("输入无效，请输入一个数字或'quit'退出。")  
  
# 退出循环后，打印一条消息  
print("谢谢使用，再见！")
