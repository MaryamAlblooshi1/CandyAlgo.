def distribute_chocolates_iterative(chocolates, students):
    """
    Distributes chocolates to students using an iterative approach.

    :param chocolates: List of dictionaries representing chocolate properties.
    :param students: List of student names.
    :return: Dictionary representing the distribution of chocolates to students.
    """
    if len(chocolates) < len(students):
        print("Not enough chocolates for all students.")
        return None
    else:
        distribution = {}
        for i in range(len(students)):
            distribution[students[i]] = chocolates[i]
        return distribution

def distribute_chocolates_recursive(chocolates, students):
    """
    Distributes chocolates to students using a recursive approach.

    :param chocolates: List of dictionaries representing chocolate properties.
    :param students: List of student names.
    :return: Dictionary representing the distribution of chocolates to students.
    """
    if len(chocolates) < len(students):
        print("Not enough chocolates for all students.")
        return None
    elif not students:
        return {}
    else:
        distribution = {}
        distribution[students[0]] = chocolates[0]
        distribution.update(distribute_chocolates_recursive(chocolates[1:], students[1:]))
        return distribution

# Test cases
chocolates = [
    {"ID": "002", "Weight": 5, "Price": 2, "Type": "Almond chocolate"},
    {"ID": "005", "Weight": 7, "Price": 4, "Type": "Peanut butter chocolate"},
    {"ID": "007", "Weight": 3, "Price": 1, "Type": "Dark chocolate"}
]
students = ["Ali", "Ahmed", "Zainab"]

# Test iterative function
print("Iterative Distribution:")
print(distribute_chocolates_iterative(chocolates, students))

# Test recursive function
print("\nRecursive Distribution:")
print(distribute_chocolates_recursive(chocolates, students))
