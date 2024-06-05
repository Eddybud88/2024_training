while True:  
    # 询问用户年龄  
    age = input("请输入您的年龄（或输入'exit'退出）：")  
      
    # 检查用户是否想退出  
    if age.lower() == 'exit':  
        break  
      
    # 尝试将输入转换为整数  
    try:  
        age = int(age)  
    except ValueError:  
        print("输入无效，请输入一个数字或'exit'退出。")  
        continue  # 如果输入无效，则继续下一次循环  
      
    # 根据年龄计算票价  
    if age < 3:  
        price = "免费"  
    elif 3 <= age <= 12:  
        price = "10 美元"  
    else:  
        price = "15 美元"  
      
    # 告诉用户他们的票价  
    print(f"您的票价是：{price}")  
  
# 退出循环后，打印一条消息  
print("谢谢使用，再见！")
