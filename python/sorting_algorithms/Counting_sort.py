def counting_sort(arr):
    n = len(arr)
    max_val = max(arr)
    count = [0] * (max_val+1)
    output = [0] * n
    for i in range(n):
        count[arr[i]] += 1
    for i in range(1, max_val+1):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return output


arr = [64,33,22,11,88,55]
if len(arr)==1 or len(arr)==2:
    print("please give more than two values")
else:
    print(counting_sort(arr))
    if counting_sort(arr)[2]%10==0:
        print("The second index of array is even")
    else:
        print("The second index of array is odd")