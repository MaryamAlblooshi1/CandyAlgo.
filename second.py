def sort_chocolates(chocolates):
    """
    Sorts chocolates first by weight and then by price.

    :param chocolates: List of dictionaries representing chocolate properties.
    """
    # Sort by weight
    chocolates.sort(key=lambda x: x["Weight"])
    # Sort by price
    chocolates.sort(key=lambda x: x["Price"])

# Test cases
chocolates = [
    {"ID": "002", "Weight": 5, "Price": 2, "Type": "Almond chocolate"},
    {"ID": "005", "Weight": 7, "Price": 4, "Type": "Peanut butter chocolate"}
]

# Sort chocolates
sort_chocolates(chocolates)

# Print sorted chocolates
print("Sorted Chocolates:")
for chocolate in chocolates:
    print(chocolate)
