while True:  
    # 获取用户输入  
    topping = input("请输入比萨配料（输入'quit'以结束）: ")  
      
    # 检查是否输入了'quit'  
    if topping.lower() == 'quit':  
        # 如果是'quit'，则结束循环  
        break  
    else:  
        # 否则，打印添加配料的消息  
        print(f"我们会在比萨中添加 {topping} 这种配料。")  
  
# 循环结束后，可以打印一条消息告诉用户输入已结束  
print("比萨配料输入结束。")
