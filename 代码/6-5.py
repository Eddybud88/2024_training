rivers = {  
    'nile': 'egypt',  
    'amazon': 'brazil',  
    'yangtze': 'china'  
}  
   
for river, country in rivers.items():  
    print(f"The {river.capitalize()} runs through {country.capitalize()}.")  

for river in rivers.keys():  
    print(river.capitalize())  

for country in rivers.values():  
    print(country.capitalize())

输出：
The Nile runs through Egypt.
The Amazon runs through Brazil.
The Yangtze runs through China.
Nile
Amazon
Yangtze
Egypt
Brazil
China
