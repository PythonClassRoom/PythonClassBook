# l is a list ordered from smallest to largest
# element is the number to find in the original list
def find(ordered_list, element_to_find):
    start_index = 1
    end_index = len(ordered_list) - 1

    while True:
        middle_index = (end_index - start_index) // 2

        if middle_index < start_index or middle_index > end_index or middle_index < 0:
            return False

        middle_element = ordered_list[middle_index]
        if middle_element == element_to_find:
            return True
        elif middle_element < element_to_find:
            end_index = middle_index
        else:
            start_index = middle_index


if __name__ == "__main__":
    l = [2, 4, 6, 8, 10]
    print(find(l, 5))  # prints False
    print(find(l, 10))  # prints True
    #print(find(l, -1))  # prints False
    print(find(l, 4))  # prints True
    #print(find(l, 2))  # prints True