修改形参：
# city_functions.py  
  
def city_country_population(city, country, population):  
    return f"{city.capitalize()}, {country.capitalize()} – population {population}"

更新测试：
# test_cities.py  
  
import unittest  
from city_functions import city_country_population  
  
class TestCityFunctions(unittest.TestCase):  
  
    def test_city_country(self):  
        # 这个测试将会失败，因为我们没有提供population参数  
        with self.assertRaises(TypeError):  
            result = city_country_population('santiago', 'chile')  
  
    # 我们需要添加新的测试方法来测试包含population的情况  
  
if __name__ == '__main__':  
    unittest.main()

将population形参设置为可选的，并为其提供一个默认值
# city_functions.py  
  
def city_country_population(city, country, population=None):  
    if population is not None:  
        return f"{city.capitalize()}, {country.capitalize()} – population {population}"  
    else:  
        return f"{city.capitalize()}, {country.capitalize()}"

更新测试：
# test_cities.py  
  
import unittest  
from city_functions import city_country_population  
  
class TestCityFunctions(unittest.TestCase):  
  
    def test_city_country_without_population(self):  
        result = city_country_population('santiago', 'chile')  
        expected = 'Santiago, Chile'  
        self.assertEqual(result, expected)  
  
    def test_city_country_with_population(self):  
        result = city_country_population('santiago', 'chile', 5000000)  
        expected = 'Santiago, Chile – population 5000000'  
        self.assertEqual(result, expected)  
  
if __name__ == '__main__':  
    unittest.main()

