模块函数：
# city_functions.py  
  
def city_country(city, country):  
    return f"{city.capitalize()}, {country.capitalize()}"

测试代码：
# test_cities.py  
  
import unittest  
from city_functions import city_country  
  
class TestCityFunctions(unittest.TestCase):  
  
    def test_city_country(self):  
        result = city_country('santiago', 'chile')  
        expected = 'Santiago, Chile'  
        self.assertEqual(result, expected)  
  
if __name__ == '__main__':  
    unittest.main()

执行测试：
python test_cities.py

结果：
.  
----------------------------------------------------------------------  
Ran 1 test in 0.000s  
  
OK

