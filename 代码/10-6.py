def get_number_input(prompt):  
    while True:  
        try:  
            return int(input(prompt))  
        except ValueError:  
            print("错误：请输入一个整数。")  
  
try:  
    # 提示用户输入第一个数字  
    num1 = get_number_input("请输入第一个数字：")  
    # 提示用户输入第二个数字  
    num2 = get_number_input("请输入第二个数字：")  
      
    # 计算两个数字的和  
    sum_of_numbers = num1 + num2  
      
    # 打印结果  
    print("两个数字的和是：", sum_of_numbers)  
except TypeError as e:   
    print("发生了一个类型错误：", e)
