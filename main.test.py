import unittest
from pprint import pprint
from main import get_open_restaurants,app

class Tests(unittest.TestCase):



    def test_get_open_restaurants(self):
        
        test_data1 = [
                "The Cowfish Sushi Burger Bar",
                "Morgan St Food Hall",
                "Beasley's Chicken + Honey",
                "Garland",
                "Crawford and Son",
                "Death and Taxes",
                "Caffe Luna",
                "Bida Manda",
                "The Cheesecake Factory",
                "Tupelo Honey",
                "Player's Retreat",
                "Glenwood Grill",
                "Neomonde",
                "Page Road Grill",
                "Mez Mexican",
                "Saltbox",
                "El Rodeo",
                "Provence",
                "Tazza Kitchen",
                "Mandolin",
                "Mami Nora's",
                "Gravy",
                "Taverna Agora",
                "Char Grill",
                "Whiskey Kitchen",
                "Sitti",
                "Stanbury",
                "Yard House",
                "David's Dumpling",
                "Gringo a Gogo",
                "Centro",
                "Brewery Bhavana",
                "Dashi",
                "42nd Street Oyster Bar",
                "Top of the Hill",
                "Jose and Sons",
                "Oakleaf",
                "Second Empire"
            ]
        
        test_data2 = [
    "The Cowfish Sushi Burger Bar",
    "Morgan St Food Hall",
    "Garland",
    "Crawford and Son",
    "Death and Taxes",
    "Bida Manda",
    "The Cheesecake Factory",
    "Tupelo Honey",
    "Player's Retreat",
    "Glenwood Grill",
    "Neomonde",
    "Page Road Grill",
    "Mez Mexican",
    "Saltbox",
    "El Rodeo",
    "Provence",
    "Tazza Kitchen",
    "Mandolin",
    "Mami Nora's",
    "Gravy",
    "Char Grill",
    "Whiskey Kitchen",
    "Sitti",
    "Yard House",
    "David's Dumpling",
    "Gringo a Gogo",
    "Centro",
    "Brewery Bhavana",
    "Dashi",
    "Top of the Hill",
    "Jose and Sons",
    "Oakleaf",
    "Second Empire"
]
        
        test_data3 = [
    "Bida Manda",
    "Tupelo Honey",
    "Glenwood Grill",
    "Neomonde",
    "Page Road Grill",
    "Whiskey Kitchen",
    "Gringo a Gogo",
    "Oakleaf"
]

        with app.app_context():
            res1 = get_open_restaurants('2024-05-04T11:00')
            self.assertEqual(res1[0].json, test_data1)
            res2 = get_open_restaurants('2024-03-02T12:30')
            self.assertEqual(res2[0].json, test_data2)
            res3 = get_open_restaurants('2024-06-07T23:00')
            self.assertEqual(res3[0].json, test_data3)
            res4 = get_open_restaurants('2024-09-02T23:30')
            self.assertEqual(res4[0].json, [])

            error_res = get_open_restaurants('Invalid Date')
            self.assertEqual(error_res[0], '''Error: Invalid Date
                Make sure the date is in the format YYYY-mm-ddTHH:MM''')
            self.assertEqual(error_res[1], 400)

    

if __name__ == '__main__':
    unittest.main()