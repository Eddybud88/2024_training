# books_module.py  
def favorite_books(title):    
    print(f"One of my favorite books is {title}.")

# 使用 import module_name    
import books_module    
    
books_module.favorite_books("Alice in Wonderland")    
    
# 使用 from module_name import function_name    
from books_module import favorite_books    
    
favorite_books("The Hobbit")    
    
# 使用 from module_name import function_name as fn    
from books_module import favorite_books as fb    
    
fb("To Kill a Mockingbird")   
    
# 使用 import module_name as mn    
import books_module as fb_module    
    
fb_module.favorite_books("1984")     
    
# 使用 from module_name import *   
from books_module import *    
  
favorite_books("The Great Gatsby")



