def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10]-1] = arr[i]
        count[index % 10] -= 1
    for i in range(n):
        arr[i] = output[i]

arr = [64,33,22,11,88,55]
if len(arr)==1 or len(arr)==2:
    print("please give more than two values")
else:
    print(radix_sort(arr))
    if radix_sort(arr)[2]%10==0:
        print("The second index of array is even")
    else:
        print("The second index of array is odd")