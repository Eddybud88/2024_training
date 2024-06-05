sandwich_orders = ['ham', 'pastrami', 'chicken', 'pastrami', 'pastrami']  
  
# 打印一条消息，指出熟食店的五香烟熏牛肉卖完了  
print("五香烟熏牛肉（pastrami）已经卖完了！")  
  
# 使用一个 while 循环将列表 sandwich_orders 中的 'pastrami' 都删除  
while 'pastrami' in sandwich_orders:  
    sandwich_orders.remove('pastrami')  
  
# 创建一个名为 finished_sandwiches 的空列表  
finished_sandwiches = []  
  
# 遍历列表 sandwich_orders  
for sandwich in sandwich_orders:  
    # 打印制作三明治的消息  
    print(f"I made your {sandwich} sandwich")  
      
    # 将制作好的三明治移到列表 finished_sandwiches  
    finished_sandwiches.append(sandwich)  
  
print("Here are the sandwiches that are ready:")  
for sandwich in finished_sandwiches:  
    print(sandwich)  

输出：
五香烟熏牛肉（pastrami）已经卖完了！
I made your ham sandwich
I made your chicken sandwich
Here are the sandwiches that are ready:
ham
chicken
The finished_sandwiches list does not contain 'pastrami'.

  
# 确认最终的列表 finished_sandwiches 中不包含 'pastrami'  
if 'pastrami' in finished_sandwiches:  
    print("Error: 'pastrami' was unexpectedly found in the finished_sandwiches list!")  
else:  
    print("The finished_sandwiches list does not contain 'pastrami'.")
