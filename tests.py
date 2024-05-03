import unittest
import main

class Tests(unittest.TestCase):
    def test_parse_days(self):
        self.assertEqual(main.parse_days('Mon-Fri'), (1,5)) 

if __name__ == '__main__':
    unittest.main()