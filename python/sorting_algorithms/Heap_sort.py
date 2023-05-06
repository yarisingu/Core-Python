def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

arr = [64,33,22,11,88,55]
if len(arr)==1 or len(arr)==2:
    print("please give more than two values")
else:
    print(heap_sort(arr))
    if heap_sort(arr)[4]%10==0:
        print("The Fourth index of array is even")
    else:
        print("The Fourth index of array is odd")