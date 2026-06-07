"""
yuntea.py

This module generates randomized drink recommendations from items from the Yun Tea House menu in San Diego, California. 

This module allows users to:
- Generate random drink base recommendations
- Generate random toppings
- Store and edit favorite menu items
- Maintain a blacklist of disliked items
- View drink descriptions
"""

import random

favorites = []
blacklist = []

# Function 1: Drink Base
def drink_base(choice):
    """
    Randomly selects a drink from the Yun Tea House menu.

    Parameters
    ----------
    choice : str 
        Drink category. Must be either "fruity" or "milk_tea".

    Returns
    -------
    str
        A randomly selected drink from chosen category. 

    Notes
    -----
    The returned drink is chosen using Python's random module, so repeated calls may produce different results.
    
    Examples
    --------
    >>> drink_base("milk_tea")
    'Peachy Princess'

    >>> drink_base("fruity")
    'Mango Sticky Rice'

    >>> drink_base("i don't know")
    "Please input 'fruity' or 'milk_tea'"

    See Also
    --------
    toppings : Randomly selects a topping
    """
    fruity = ["Freshly-Squeezed Orange", 
          "Mango Sticky Rice", 
          "Hojicha Snow", 
          "Matcha Made in Heaven", 
          "Salt + Strawberry"
            ]
    
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

    # Using .lower() because capitalization matters in parameters/variables, using this method helps keep inputs consistent and less work for users
    if choice.lower() == "fruity":
        out = random.choice(fruity)
    elif choice.lower() == "milk_tea":
        out = random.choice(milk_tea)
    else:
        out = "Please input 'fruity' or 'milk_tea'"

    return out

# Function 2: Toppings
def toppings(choice):
    """
    Randomly selects a topping for a drink.

    Parameters
    ----------
    choice : str
        Either "yes" to get a topping or "no" for no toppings.

    Returns
    -------
    str or None
        A randomly selected topping if choice is "yes".
        Returns None if choice is "no". 
        Returns an error message if input is invalid.

    Notes
    -----
    The topping is selected randomly using the random module, so repeated calls may produce different results

    Examples
    --------
    >>> toppings("yes")
    'Boba'

    >>> toppings ("no")
    None

    >>> toppings("maybe")
    "Please input 'yes' or 'no'"

    See Also
    --------
    drink_base : Randomly selects a drink base
    """
    toppings_list = ["Aiyu Jelly", 
            "Grass Jelly", 
            "Boba", 
            "Pudding", 
            "Sticky Rice", 
            "Barley Popping Boba", 
            "Black Sesame Popping Boba"
            ]
    
    if choice.lower() == "yes":
        out = random.choice(toppings_list)
    elif choice.lower() == "no":
        out = None
    else:
        out = "Please input 'yes' or 'no'"

    return out

# Function 3: Add Favorite Items to a List
def add_favorites(item):
    """
    Adds an item to the favorites list.

    Parameters
    ----------
    item : str
        The name of the item to add.

    Returns
    -------
    list
        The updated list of favorite items.

    Notes
    -----
    Duplicate items are not added to the favorites list. If the item already exists in favorites, the list remains unchanged.

    Examples
    --------
    >>> favorites = []
    >>> add_favorites("Boba")
    ['Boba']

    >>> add_favorites("Boba")
    ['Boba']

    >>> add_favorites("Peachy Princess")
    ['Boba', 'Peachy Princess']

    See Also
    --------
    remove_favorite : Removes an item from the favorites list.
    add_blacklist : Adds an item to the blacklist.
    """
    # The parameter 'item' is used in favorites because users have the ability to add their favorite drink bases and toppings
    if item not in favorites:
        favorites.append(item)

    return favorites

# Function 4: Add Bad Items to a Blacklist
def add_blacklist(item):
    """
    Adds an item to the blacklist.

    Parameters
    ----------
    item : str
        The name of the item that will be blacklisted.

    Returns
    -------
    list
        The updated blacklist.

    Notes
    -----
    Duplicate items are not added to the blacklist. If the item already exists in the blacklist, the list remains unchanged.

    Examples
    --------
    >>> blacklist = []
    >>> add_blacklist("Boba")
    ['Boba']

    >>> add_blacklist("Boba")
    ['Boba']

    >>> add_blacklist("Grass Jelly")
    ['Boba', 'Grass Jelly']
    """
    # The parameter 'item' is used in the blacklist because users have the ability to add their disliked drink bases and toppings
    if item not in blacklist:
        blacklist.append(item)

    return blacklist

# Function 5: Get Descriptions About Drinks (Drink Bases)
def get_description(drink):
    """
    Retrieves a description for a drink.

    Parameters
    ----------
    drink : str
        The name of the drink.

    Returns
    -------
    str
        The drink description. 
        Returns 'No description available.' if drink is not found in descriptions dictionary.

    Notes
    -----
    Descriptions are only available for drink bases. Toppings don't have descriptions.

    The function uses the dictionary .get() method to retrieve descriptions without raising a KeyError.

    Examples
    --------
    >>> get_description("Dark Phoenix")
    'Originated from the Phoenix Mountains in Guangdong, China, the fragrant phoenix oolong milk tea has a darker shade and stronger fruity aroma.'

    >>> get_description("Boba")
    'No description available'
    """
    descriptions = {"Dark Phoenix" : "Originated from the Phoenix Mountains in Guangdong, China, the fragrant phoenix oolong milk tea has a darker shade and stronger fruity aroma.", 
                "Duck Sh*t" : "An oolong tea that has a sharp and sweet profile with a slight gardenia aroma. Its special name comes from the fact it was a very special tea to farmers, hence why they gave this tea a strange name so thieves would stay away.", 
                "Emperor's Red Robe" : "Directly translated from its Chinese name 'Da Hong Pao', this oolong tea is especially fragrant with its unique orchid flavor and its sweet aftertaste. It's known as one of the most naturally fragrant teas.", 
                "Monkey King" : "Based on the Golden Monkey Tea, this black tea has cocoa notes along with slight fruitiness and scents of spices creating a velvety milk tea.", 
                "Iron Goddess" : "From a type of Chinese tea, 'Tie Guan Yin', its oolong flavor is notable for its bright floral taste.", 
                "Dragon Well" : "Originating from the misty hills of Hangzhou, this green tea gets its lingering sweetness from its delicate balance of profiles of fresh grassy notes and mellow roasted chestnuts.", 
                "Peachy Princess" : "Peach is considered the best oolong tea fruit pairing as the white peach magnifies the already-fragrant notes of oolong with more fruity notes.", 
                "Snow Jasmine" : "A Jasmine tea blend enhanced by adding extra jasmine flowers for floral aroma in the brew, giving the appearance of the tea being mixed in snow.", 
                "Roasted Oolong" : "The perfect ratio of oolong and hojicha: chocolate, nutty, and earthy taste with woodsy undertones.", 
                "Hojicha" : "An aromatic Japanese roasted green tea with milk. A taste of harmonious balance of nutty undertones and silky sweetness.", 
                "Genmaicha" : "A roasted rice drink that gives a warm nutty flavor with grassy notes from the Japanese green tea.", 
                "ZzZ" : "A non-caffeinated tea from South Africa with sweet, grassy, vanilla, and floral flavor profiles.", 
                "Freshly-Squeezed Orange" : "Orange juice with a choice of tea. Recommended teas: Duck Sh*t, Emperor's Red Robe, Snow Jasmine", 
                "Mango Sticky Rice" : "Classic Thai dessert in slushie form. A sweet mango base with chewy sticky rice topped with butter cloud.", 
                "Hojicha Snow" : "If the song of ice and fire were a drink. A vanilla sky with butter cloud on top of blended hojicha.", 
                "Matcha Made in Heaven" : "A blended matcha icy base with vanilla sky and butter cloud.", 
                "Salt + Strawberry" : "Blended strawberry drink contrasted with grassy matcha and umami miso cloud."
                }
    
    # In this function, the parameter is 'drink' because there are only descriptions for the drink bases, not for toppings
    return descriptions.get(drink, "No description available.")

# Function 6: Remove Item from Favorites
def remove_favorite(item):
    """
    Removes an item from the favorites list.

    Parameters
    ----------
    item : str
        The item to remove.

    Returns
    -------
    list
        The updated favorites list.

    Notes
    -----
    If the item is not present, the favorites list is unchanged.

    Examples
    --------
    >>> favorites = ["Boba", "Dark Phoenix"]
    >>> remove_favorite("Boba")
    ['Dark Phoenix']

    >>> remove_favorite("Grass Jelly")
    ['Dark Phoenix']

    >>> remove_favorite("Dark Phoenix")
    []
    """
    # Having functions with .remove() makes recommendations more flexible and customizable to individuals who uses this module 
    if item in favorites:
        favorites.remove(item)

    return favorites

# Function 7: Remove Item from Blacklist
def remove_blacklist(item):
    """
    Removes an item from the blacklist.

    Parameters
    ----------
    item : str
        The item to remove.

    Returns
    -------
    list
        The updated blacklist.

    Notes
    -----
    If the item is not present, the blacklist is unchanged.

    Examples
    --------
    >>> blacklist = ["Boba", "Grass Jelly"]
    >>> remove_blacklist("Boba")
    ['Grass Jelly']

    >>> remove_blacklist("Pudding")
    ['Grass Jelly']

    >>> remove_blacklist("Grass Jelly")
    []

    See Also
    --------
    add_blacklist : Adds an item to the blacklist
    remove_favorite : Removes an item from the favorites list.
    """
    if item in blacklist:
        blacklist.remove(item)

    return blacklist

    
