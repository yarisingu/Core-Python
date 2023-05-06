def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

arr = [64,33,22,11,88,55]
if len(arr)==1 or len(arr)==2:
    print("please give more than two values")
else:
    print(merge_sort(arr))
    if merge_sort(arr)[3]%10==0:
        print("The Third index of array is even")
    else:
        print("The Third index of array is odd")