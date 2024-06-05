car_type = input("请输入您想要租赁的汽车类型：")  
  
# 检查用户输入的汽车类型，并打印相应的消息  
if car_type.lower() == "subaru":  
    print("让我看看是否能为您找到一辆Subaru。")   
else:  
    print(f"让我看看是否能为您找到一辆{car_type}。") 

输出：
请输入您想要租赁的汽车类型：subaru
让我看看是否能为您找到一辆Subaru。
