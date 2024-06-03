places = ['London' , 'Paris' , 'Tokyo' , 'Hongkong' , 'Berlin']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort() 
print(places)
places.sort(reverse=True) 
print(places)

输出：
['London', 'Paris', 'Tokyo', 'Hongkong', 'Berlin']
['Berlin', 'Hongkong', 'London', 'Paris', 'Tokyo']
['London', 'Paris', 'Tokyo', 'Hongkong', 'Berlin']
['Tokyo', 'Paris', 'London', 'Hongkong', 'Berlin']
['London', 'Paris', 'Tokyo', 'Hongkong', 'Berlin']
['Berlin', 'Hongkong', 'Tokyo', 'Paris', 'London']
['London', 'Paris', 'Tokyo', 'Hongkong', 'Berlin']
['Berlin', 'Hongkong', 'London', 'Paris', 'Tokyo']
['Tokyo', 'Paris', 'London', 'Hongkong', 'Berlin']
