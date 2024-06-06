def order_sandwich(*ingredients):  
    # 将食材列表转换为字符串，并用逗号分隔  
    ingredients_string = ', '.join(ingredients)  
    # 打印一条消息概述三明治  
    print(f"Your sandwich includes: {ingredients_string}")  
  
# 调用函数三次，每次都提供不同数量的实参  
order_sandwich('ham', 'cheese', 'lettuce')  
order_sandwich('turkey', 'avocado', 'tomato', 'bacon')  
order_sandwich('veggie', 'hummus', 'cucumber', 'red onion', 'sprouts')

输出：
Your sandwich includes: ham, cheese, lettuce
Your sandwich includes: turkey, avocado, tomato, bacon
Your sandwich includes: veggie, hummus, cucumber, red onion, sprouts
