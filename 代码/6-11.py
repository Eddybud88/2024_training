# 创建一个名为 cities 的字典  
cities = {  
    'Tokyo': {  
        'country': 'Japan',  
        'population': '13,986,000', 
        'fact': 'Tokyo is the capital and most populous city of Japan.'  
    },  
    'New York': {  
        'country': 'United States',  
        'population': '8,398,748',    
        'fact': 'New York is the most populous city in the United States.'  
    },  
    'London': {  
        'country': 'United Kingdom',  
        'population': '9,304,016',  
        'fact': 'London is the capital and largest city of England and the United Kingdom.'  
    }  
}  
  
for city, info in cities.items():  
    print(f'City: {city}')  
    print(f'Country: {info["country"]}')  
    print(f'Population: {info["population"]}')  
    print(f'Fact: {info["fact"]}')  
    print() 

输出：
City: Tokyo  
Country: Japan  
Population: 13,986,000  
Fact: Tokyo is the capital and most populous city of Japan.  
  
City: New York  
Country: United States  
Population: 8,398,748  
Fact: New York is the most populous city in the United States.  
  
City: London  
Country: United Kingdom  
Population: 9,304,016  
Fact: London is the capital and largest city of England and the United Kingdom.
