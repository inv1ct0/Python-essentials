# Бинарный поиск

def binary_search(arr, item):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 4, 5, 12, 14, 18, 21, 22, 26]

print(binary_search(my_list, 5))
