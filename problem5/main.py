def remove_duplicates(array):
    if not array:
        return 0
    
    unique_pointer = 0

    for i in range(1, len(array)):
        if array[i] != array[unique_pointer]:
            unique_pointer += 1
            array[unique_pointer] = array[i]

    return unique_pointer + 1

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) # 6
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([1, 2, 3, 11, 11])) # 4