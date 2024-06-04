favorite_numbers = {    
    'Alice': [9, 7, 2],    
    'Bob': [153, 3, 5],    
    'Charlie': [432, 67, 10],    
    'David': [11, 22, 33],    
    'George': [23, 12, 3]    
}    
    
for name, numbers in favorite_numbers.items():    
    print(f"{name} 喜欢的数字是：", end=' ')  
    for number in numbers:  
        print(number, end=' ')  
    print()  

输出：
Alice 喜欢的数字是： 9 7 2   
Bob 喜欢的数字是： 153 3 5   
Charlie 喜欢的数字是： 432 67 10   
David 喜欢的数字是： 11 22 33   
George 喜欢的数字是： 23 12 3
