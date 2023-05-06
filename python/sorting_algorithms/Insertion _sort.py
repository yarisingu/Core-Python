def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
arr = [64,33,22,11,88,55]
if len(arr)==1 or len(arr)==2:
    print("please give more than two values")
else:
    print(insertion_sort(arr))
    if insertion_sort(arr)[1]%10==0:
        print("The First index of array is even")
    else:
        print("The First index of array is odd")