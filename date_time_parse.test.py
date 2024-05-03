import unittest
from date_time_parse import break_down_hours,parse_date_range,unabbreviate_time,format_time,parse_time,parse_restaurant_hours,find_restaurant_hours
class Tests(unittest.TestCase):
    def test_break_down_hours(self):
        self.assertEqual(break_down_hours('Mon-Fri, Sat 11 am - 12 pm  / Sun 11 am - 10 pm'), ['Mon-Fri, Sat 11 am - 12 pm', 'Sun 11 am - 10 pm']) 
    def test_parse_date_range(self):
        self.assertEqual(parse_date_range('Mon-Fri'), [1,2,3,4,5]) 
    def test_unabbreviate_time(self):
        self.assertEqual(unabbreviate_time('11'), '11:00') 
    def test_format_time(self):
        self.assertEqual(format_time('11 am'), '11:00') 
        self.assertEqual(format_time('11 pm'), '23:00') 
    def test_parse_time(self):
        self.assertEqual(parse_time('5:30 pm - 11 pm'), (17,30,23,0)) 
    def test_parse_restaurant_hours(self):
        self.assertEqual(parse_restaurant_hours(time='11 am - 12 pm',date_range='Mon-Fri',day= 'Sat'), ([1,2,3,4,5,6],(11,0,12,0))) 
    def test_find_restaurant_hours(self):
        self.assertEqual(find_restaurant_hours('Mon-Fri, Sat 11 am - 12 pm'), ([1,2,3,4,5,6],(11,0,12,0))) 
        self.assertEqual(find_restaurant_hours('Mon-Fri 1:30 pm - 4 pm'), ([1,2,3,4,5,],(13,30,16,0))) 
        self.assertEqual(find_restaurant_hours('Mon 7:30 am - 4:45 pm'), ([1],(7,30,16,45))) 
        self.assertEqual(find_restaurant_hours('Tues, Fri-Sun 7 am - 8 am'), ([5,6,7,2],(7,0,8,0))) 
        
        with self.assertRaises(Exception) as context: 
            find_restaurant_hours('')
        self.assertTrue('String not found' in str(context.exception))

if __name__ == '__main__':
    unittest.main()