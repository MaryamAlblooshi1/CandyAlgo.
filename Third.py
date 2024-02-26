def search_chocolate(chocolates, target_weight):
    """
    Searches for a chocolate with a specific weight.

    :param chocolates: List of dictionaries representing chocolate properties.
    :param target_weight: Weight to search for.
    :return: Dictionary representing the found chocolate or None if not found.
    """
    for chocolate in chocolates:
        if chocolate["Weight"] == target_weight:
            return chocolate
    return None

# Test cases
chocolates = [
    {"ID": "002", "Weight": 5, "Price": 2, "Type": "Almond chocolate"},
    {"ID": "005", "Weight": 7, "Price": 4, "Type": "Peanut butter chocolate"}
]

# Search for a chocolate with weight 7
print("Chocolate with weight 7:", search_chocolate(chocolates, 7))

# Search for a chocolate with weight 10
print("Chocolate with weight 10:", search_chocolate(chocolates, 10))
