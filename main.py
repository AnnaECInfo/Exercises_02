def count_integer(numbers, integer):
    occurrence = 0
    if integer in numbers:
        for integer in numbers:
            occurrence = occurrence + 1
        return occurrence
    else:
        return 42

def list_func(numbers, integer):
    if integer in numbers:
        numbers_two = numbers.copy()
        replace_index = numbers_two.index(integer)
        numbers_two.remove(integer)
        numbers_two.insert(replace_index, 6)
        reversed_list = list(reversed(numbers_two))
        print(reversed_list)
        return numbers_two
    else:
        return []

def compare_lists(list1, list2):
    new_list = set(list1).intersection(set(list2))
    if new_list:
        print(list(new_list))
    else:
        print(list())

def remove_duplicates(lst):
    if len(set(lst)) == len(lst):
        return lst
    else:
        new_list = set(lst)
        return list(new_list)

def dict_func(dictionary):
    dictionary.keys = {'Type', 'Brand', 'Price'}
    print(f"You have a {dictionary['Type']} from {dictionary['Brand']} that costs {dictionary['Price']}")
    dictionary["OS"] = "Linux"
    print(dictionary)
    if {'Type'} not in dictionary.keys:
        dictionary.update({'Type': f"unknown type"})
        print(f"You have a {dictionary['Type']} from {dictionary['Brand']} that costs {dictionary['Price']}")
    if {'Brand'} not in dictionary.keys:
        dictionary.update({'Brand': f"unknown brand"})
        print(f"You have a {dictionary['Type']} from {dictionary['Brand']} that costs {dictionary['Price']}")
    if {'Price'} not in dictionary.keys:
        dictionary.update({'Price': f"unknown price"})
        print(f"You have a {dictionary['Type']} from {dictionary['Brand']} that costs {dictionary['Price']}")
    return dictionary

