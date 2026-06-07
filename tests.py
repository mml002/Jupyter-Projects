"""Unit tests to test functionality of project.
"""

import unittest
import yuntea

class TestYunTea(unittest.TestCase):

    def setUp(self):
        """
        Reset favorites and blacklist before each test.
        """
        yuntea.favorites.clear()
        yuntea.blacklist.clear()

    #Function 1: drink_base
    def test_drink_base_fruity(self):
        drink = yuntea.drink_base("fruity")

        fruity = ["Freshly-Squeezed Orange", 
          "Mango Sticky Rice", 
          "Hojicha Snow", 
          "Matcha Made in Heaven", 
          "Salt + Strawberry"
            ]

        self.assertIn(drink, fruity)

    def test_drink_base_milk_tea(self):
        drink = yuntea.drink_base("milk_tea")

        milk_tea = ["Dark Phoenix", 
            "Duck Sh*t", 
            "Emperor's Red Robe", 
            "Monkey King", 
            "Iron Goddess", 
            "Dragon Well", 
            "Peachy Princess", 
            "Snow Jasmine", 
            "Roasted Oolong", 
            "Hojicha", 
            "Genmaicha", 
            "ZzZ"
            ]

        self.assertIn(drink, milk_tea)

    def test_drink_base_invalid(self):
        self.assertEqual(yuntea.drink_base("coffee"), "Please input 'fruity' or 'milk_tea'")

    #Function 2: toppings
    def test_toppings_yes(self):
        topping = yuntea.toppings("yes")

        toppings = ["Aiyu Jelly", 
            "Grass Jelly", 
            "Boba", 
            "Pudding", 
            "Sticky Rice", 
            "Barley Popping Boba", 
            "Black Sesame Popping Boba", 
            ]

        self.assertIn(topping, toppings)

    def test_toppings_no(self):
        self.assertIsNone(yuntea.toppings("no"))

    def test_toppings_invalid(self):
        self.assertEqual(yuntea.toppings("maybe"), "Please input 'yes' or 'no'")

    #Function 3: add_favorites
    def test_add_favorites(self):
        yuntea.add_favorites("Dragon Well")

        self.assertIn("Dragon Well", yuntea.favorites)

    def test_add_favorites_no_dupes(self):
        yuntea.add_favorites("Dragon Well")
        yuntea.add_favorites("Dragon Well")

        self.assertEqual(len(yuntea.favorites), 1)

    #Function 4: add_blacklist
    def test_add_blacklist(self):
        yuntea.add_blacklist("Duck Sh*t")

        self.assertIn("Duck Sh*t", yuntea.blacklist)

    def test_add_blacklist_no_dupes(self):
        yuntea.add_blacklist("Duck Sh*t")
        yuntea.add_blacklist("Duck Sh*t")

        self.assertEqual(len(yuntea.blacklist), 1)

    #Function 5: get_description
    def test_get_description_exists(self):
        description = yuntea.get_description("Matcha Made in Heaven")

        self.assertIn("A blended matcha icy base with vanilla sky and butter cloud.", description)

    def test_get_description_missing(self):
        self.assertEqual(yuntea.get_description("Coffee"), "No description available.")

    #Function 6: remove_favorites
    def test_remove_favorite(self):
        yuntea.add_favorites("Dragon Well")
        yuntea.remove_favorite("Dragon Well")

        self.assertNotIn("Dragon Well", yuntea.favorites)

    def test_remove_favorite_not_present(self):
        yuntea.remove_favorite("Dragon Well")
        self.assertEqual(yuntea.favorites, [])

    #Function 7: remove_blacklist
    def test_remove_blacklist(self):
        yuntea.add_blacklist("Duck Sh*t")
        yuntea.remove_blacklist("Duck Sh*t")

        self.assertNotIn("Duck Sh*t", yuntea.blacklist)

    def test_remove_blacklist_not_present(self):
        yuntea.remove_blacklist("Duck Sh*t")
        self.assertEqual(yuntea.blacklist, [])

        
    







                 
    