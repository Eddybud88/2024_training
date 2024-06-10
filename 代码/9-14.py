import random  
  
class Die:  
    def __init__(self, sides=6):  
        self.sides = sides  
  
    def roll_die(self):  
        return random.randint(1, self.sides)  
  
    def roll_many_times(self, num_rolls):  
        for _ in range(num_rolls):  
            print(self.roll_die(), end=' ')  
        print()    
  
# 创建一个6面的骰子，并掷10次  
six_sided_die = Die(6)  
six_sided_die.roll_many_times(10)  
  
# 创建一个10面的骰子，并掷10次  
ten_sided_die = Die(10)  
ten_sided_die.roll_many_times(10)  
  
# 创建一个20面的骰子，并掷10次  
twenty_sided_die = Die(20)  
twenty_sided_die.roll_many_times(10)
