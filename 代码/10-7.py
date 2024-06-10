def get_number_input(prompt):  
    while True:  
        try:  
            return int(input(prompt))  
        except ValueError:  
            print("错误：请输入一个整数。")  
  
# 提示用户输入两个数字  
print("请输入两个数字以计算它们的和：")  
  
num1 = get_number_input("请输入第一个数字：")  
num2 = get_number_input("请输入第二个数字：")  
  
# 计算两个数字的和  
sum_of_numbers = num1 + num2  
  
# 打印结果  
print("两个数字的和是：", sum_of_numbers)
