def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Пример использования
unsorted_list = [1, 12, 14, 18, 16, 21, 22, 28, 32, 33, 37, 39, 40, 42, 45, 48, 50]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

def binary_search(search_element, list_to_search: list):
    pos = 0
    result_ok = False
    first = 0
    last = len(list_to_search) - 1
    while first <= last:
        middle = (first + last) // 2
        if search_element == list_to_search[middle]:
            first = middle
            last = first - 1
            result_ok = True
            pos = middle
        elif search_element > list_to_search[middle]:
            first = middle + 1
        else:
            last = middle - 1
    if result_ok:
        print(f'The element is found, position: {pos}')
    else:
        print(f'The element is not found')
binary_search(42, sorted_list)