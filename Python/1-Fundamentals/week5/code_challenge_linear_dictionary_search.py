def linear_search_dictionary(dictionary, target):
    for x, y in dictionary.items():
        if y == target:
            print("success, found at key " + str(y))
            return x
    print("failure")
    return None

my_dictionary = {"red": 5, "blue": 3, "green":7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)