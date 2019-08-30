# l is a list ordered from smallest to largest
# element is the number to find in the original list
def find(ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
    return False


if __name__ == "__main__":
    l = [2, 4, 6, 8, 10]
    print(find(l, 5))  # prints False
    print(find(l, 10))  # prints True
    print(find(l, -1))  # prints False
    print(find(l, 2))  # prints True