sandwich_orders = ['ham', 'cheese', 'chicken']  
  
finished_sandwiches = []  
  
# 遍历列表 sandwich_orders  
for sandwich in sandwich_orders:  
    print(f"I made your {sandwich} sandwich")  
      
    finished_sandwiches.append(sandwich)  
  
# 所有三明治都制作好后，打印一条消息，将这些三明治列出来  
print("Here are the sandwiches that are ready:")  
for sandwich in finished_sandwiches:  
    print(sandwich)

输出：
I made your ham sandwich
I made your cheese sandwich
I made your chicken sandwich
Here are the sandwiches that are ready:
ham
cheese
chicken
