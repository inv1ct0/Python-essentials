# Сортировка выбором

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    selected_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        selected_arr.append(arr.pop(smallest))
    return selected_arr


my_list = [1, 5, 2, 45, 16, 29, 58, 43, 36, 99, 3]
print(selection_sort(my_list))
