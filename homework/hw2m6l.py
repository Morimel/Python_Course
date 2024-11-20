large_list = [1, 5, 10, 15, 20, 25, 27, 30, 35, 40]
def selection_sort(array):
    array_length = len(array)
    while array_length > 0:
        array_length -= 1
        biggest_number = array[0]
        for num in array[:array_length + 1]:
            if num > biggest_number:
                biggest_number = num 
        index_to_move = array.index(biggest_number)
        array[index_to_move], array[array_length] = array[array_length], array[index_to_move]
    return array
    
print(selection_sort(large_list))

def binary_sort(array, val):
    resultOk = False
    first = 0 
    last = len(array) - 1  
    pos = -1  
    
    while first <= last:
        middle = (first + last) // 2 
        if val == array[middle]:  
            resultOk = True
            pos = middle
            break  
        elif val > array[middle]:  
            first = middle + 1
        else:  
            last = middle - 1
    
    if resultOk:
        print(f"Элемент найден на позиции {pos}")
    else:
        print("Элемент не найден")

binary_sort(large_list, 35)
